import csv
import os
import numpy as np
from astropy.table import Table
from matplotlib import pyplot as plt


FILE_PATH = "../../data/soil_spectra/exported_ICRAF_database/spectra.TXT"
DIR_PATH = os.path.dirname(__file__)
ABS_PATH = os.path.join(DIR_PATH, FILE_PATH)


def read_spectra_database_csv():
    with open(FILE_PATH, newline='') as csvfile:
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


def plot_database(tbl):
    x = tbl["wavelength"]
    for colname in tbl.colnames[1:]:
        y = tbl[colname].data
        plt.plot(x, y)


my_tbl = read_spectra_database_csv()
plot_database(my_tbl)
plt.show()