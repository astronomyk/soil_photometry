Notes
=====

The ICRAF database can be opened and exported to TXT with this:
https://www.netzwelt.de/software-download/18341-mdb-viewer-plus.html

Question about soil pH values
-----------------------------
.. admonition:: Question

   The database gives two values for soil pH for some locations: PHH2O, PHKCL.
   The question is: what is the relationship between these two? Becasue when
   plotted they don't correlate
   well.

.. plot::

   import matplotlib.pyplot as plt
   from astropy.table import Table
   tbl = Table.read("../../../data/soil_spectra/exported_ICRAF_database/chemical_properties.TXT", format="csv")
   plt.plot(tbl["PHH2O"], tbl["PHKCL"], ".")
   plt.plot([2,11], [2,11], "k:")
   plt.xlabel("pH (H2O)")
   plt.ylabel("pH (KCl)")