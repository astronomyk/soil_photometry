import csv
import os
import numpy as np
from astropy.table import Table
from astropy.io import fits
from matplotlib import pyplot as plt

REL_PATH = "../../data/soil_spectra/exported_ICRAF_database/"
DIR_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), REL_PATH))


def read_csv(filename):
    return Table.read(filename=os.path.join(DIR_PATH, filename), format="csv")


tbl = read_csv("chemical_properties.TXT")

for col in tbl.colnames:
    tbl[col] = np.nan_to_num(np.array(tbl[col]))

ii = 0
while ii < len(tbl["SAMPLENO"]):
    if not np.char.isnumeric(tbl["SAMPLENO"][ii]):
        tbl.remove_row(ii)
    else:
        ii += 1

print(np.unique(tbl["SAMPLENO"]))

tbl["SAMPLENO"].data = tbl["SAMPLENO"].data.astype(int)
print(fits.table_to_hdu(tbl).data)

