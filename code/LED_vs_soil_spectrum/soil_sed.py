import numpy as np
from matplotlib import pyplot as plt
from astropy.io import ascii
from scipy.interpolate import interp1d
from scipy.stats import norm


def plot_gaussian(peak, fwhm, height=100, **kwargs):
    sig = fwhm / 2.35
    x = np.linspace(peak - 3 * sig, peak + 3 * sig, 101)
    y = norm.pdf(x, peak, sig)
    plt.plot(x, height * y / np.max(y), **kwargs)


spec = ascii.read("""
wave    refl
500     32
550     42
850     60
1000    62
1350    73
1400    63
1650    80
1850    80
1900    52
2100    74
2150    78
2225    64
2250    67
2350    67
2500    46
""")

x, y = spec["wave"], spec["refl"]
soil_sed = interp1d(x, y, kind="slinear")

ushio_leds = np.array([375, 385, 395, 405, 415, 420, 430, 450, 470, 490, 505,
                       525, 545,  565,  570,  590,  600,  610,  625,  630,  645,
                       660, 670,  680,  690,  700,  720,  730,  735,  740,
                       750,  760,  770, 780,  800,  805,  810,  820,  830,
                       840,  850,  870,  880,  890, 910,  940,  970,  980,
                       1050, 1070, 1200, 1300, 1450, 1550, 1650])

eoc_leds = np.array([1.65 , 1.735, 1.845, 1.945, 2.045, 2.145, 2.245, 2.345,
                     3.395, 3.395, 3.595, 3.77, 4.02, 4.2, 4.5]) * 1e3

plt.figure(figsize=(12, 4))

mask1 = (ushio_leds > 500) * (ushio_leds < 900)
mask2 = (ushio_leds > 900)
ushio = np.array(list(ushio_leds[mask1])[::5] + list(ushio_leds[mask2]))
for wave in ushio:
    fwhm = wave / 10.
    plot_gaussian(wave, fwhm, 40, c="b", alpha=0.3)
    plt.axvline(wave, ls=":", c="b", alpha=0.2)


eoc = eoc_leds[eoc_leds < 2700]
for wave in eoc:
    fwhm = wave / 8.
    plot_gaussian(wave, fwhm, 40, c="g", alpha=0.3)
    if wave < np.max(x):
        plt.axvline(wave, ls=":", c="g", alpha=0.2)


xn = np.linspace(min(x), max(x), 100)
plt.plot(xn, soil_sed(xn) + 10, c="k", label="true spectrum")
plt.plot(ushio, soil_sed(ushio)-10, "ro-", alpha=0.5)
plt.plot(eoc, soil_sed(eoc)-10, "ro-", alpha=0.5, label="reconstructed spectrum")

plt.legend(loc=2)
plt.ylim(0, 100)
plt.xlabel("Wavelength [nm]")
plt.ylabel("Reflectivity [%]")

plt.savefig("LEDs_vs_soil_spectrum.svg", format="svg")
plt.savefig("LEDs_vs_soil_spectrum.png", format="png")

#plt.show()
