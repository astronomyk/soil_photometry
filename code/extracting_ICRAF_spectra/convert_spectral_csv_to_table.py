import csv
import os
import numpy as np
from astropy.table import Table
from astropy.io import fits
from matplotlib import pyplot as plt

import warnings
from astropy.utils.exceptions import AstropyWarning

warnings.simplefilter('ignore', AstropyWarning)


REL_PATH = "../../data/soil_spectra/exported_ICRAF_database/"
DIR_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), REL_PATH))


def read_csv(filename):
    return Table.read(filename=os.path.join(DIR_PATH, filename), format="csv")


def read_spectra_csv():
    filename = "spectra.TXT"
    with open(os.path.join(DIR_PATH, filename), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        names, data = [], []
        for row in spamreader:
            names += [row[0]]
            data += [row[1:]]

        data[0] = [np.float(wave.replace("W", "")) for wave in data[0]]
        names[0] = "wavelength"
        data = np.array(data).astype(float).T

    tbl = Table(names=names, data=data)
    return tbl


def convert_to_coords(sample_row):
    sns = 1 if sample_row["LATNS"] == "N" else -1
    sew = 1 if sample_row["LONEW"] == "E" else -1
    lat = sample_row["LATD"] + sample_row["LATM"]/60 + sample_row["LATS"]/3600
    lon = sample_row["LOND"] + sample_row["LONM"]/60 + sample_row["LONS"]/3600

    return sns * lat, sew * lon


def add_extra_data(samp_no, tbl, suffix, silent=True):
    return {}


def make_bintablehdu(sample_row, spec_tbl, extra_tbls={}, n=None):
    if n is not None and n % 10 == 0:
        print(n)

    samp_no = sample_row["Chemical_properties.SAMPLENO"]
    lab_name = sample_row["Batch and labid"]

    data = Table(data=[spec_tbl["wavelength"].data, spec_tbl[lab_name].data],
                 names=["wavelength", "reflectivity"])
    hdr_dict = {"ID": samp_no,
                "lab_name": lab_name,
                "country": sample_row["Plotcode"][:2],
                "plotcode": sample_row["Plotcode"],
                "DSED": sample_row["Dsed"]}

    hdu = fits.table_to_hdu(data)
    hdu.header.update(hdr_dict)

    lat, lon = convert_to_coords(sample_row)
    try:
        hdu.header.update({"latitude": lat, "longitud": lon})
    except:
        print(f"Coords: {(lat, lon)} couldn't be added to header")

    for key in extra_tbls:
        tbl = extra_tbls[key]
        print(type(tbl["SAMPLENO"].data), type(samp_no))
        ii = np.where(tbl["SAMPLENO"] == samp_no)[0]
        if len(ii) > 1:
            ii = ii[:1]
        if len(ii) > 0:
            ii = ii[0]

            for col in tbl.colnames:
                if col not in ["ISO", "ID", "HORI", "TOP", "BOT", "SAMPLENO",
                               "EDITDATE", "VERIFIED"]:
                    val = tbl[col][ii]
                    print(col, type(val), val)
                    if isinstance(val, np.float):
                        val = float(val)
                    elif isinstance(val, np.int):
                        val = int(val)
                    else:
                        val = str(val)[:40]
                        if val == "--" or val == "":
                            continue

                    try:
                        hdu.header[f"{key}_{col}"] = val
                    except:
                        print(f"{samp_no}:{key}:{col} = {val}"
                              f" was not added to header")

    return hdu


sample_ids = read_csv("sample_data.TXT")
spectra = read_spectra_csv()

extra_tbls = {"CHEM": read_csv("chemical_properties.TXT"),
              "SAND": read_csv("sand_minerology.TXT"),
              "SOIL": read_csv("soil_composition.TXT"),
              "CLAY": read_csv("clay_composition.TXT"),
              "SALT": read_csv("soluble_salts.TXT")}

hdu_list = []
for n, row in enumerate(sample_ids[:20]):
    hdu = make_bintablehdu(row, spectra, extra_tbls, n)
    if hdu is not None:
        hdu.writeto(f"{n}.fits", overwrite=True)
        hdu_list += [hdu]
hdu_list = fits.HDUList(hdu_list)
hdu_list.writeto("soil_spectra.fits", overwrite=True)
