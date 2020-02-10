Real-time in-situ measurements of soil properties with Visual-NIR spectro-photometry
====================================================================================
3rd / Final Draft

Title with 60 characters: Real-time in-situ soil properties with NIR spectro-photometry

Deutscher Titel: Echtzeit in-situ Bodenmessungen mit NIR Spektrophotometrie

FWF 1000 Ideas Funding Programme

Deadline 15. January 2020

PI: Prof. João Alves (IfA)

CoI: Prof. Walter Wenzel (BOKU), Kieran Leschinski (IfA)

Academic abstract
-----------------
(max 700 characters incl. headings)

Research questions/hypotheses
+++++++++++++++++++++++++++++
Is it possible to combine astronomy with soil science in a bid to fight climate change? Can astronomical spectro-photometry techniques be used effectively in soil science to efficiently determine soil properties in-situ and in real-time?

Intended approaches and research design
+++++++++++++++++++++++++++++++++++++++
Low-resolution spectroscopy can be mimicked by sequentially illuminating soil samples with multi-wavelength LED arrays. Soil properties can, therefore, be determined by mapping the LED wavelengths to certain characteristic spectral tracers.

Expected results
++++++++++++++++
The foundations for the development of efficient miniaturised in-situ real-time non-destructive soil property sensors.

Research approach
-----------------
Scientific foundation
+++++++++++++++++++++
What enables life on earth is 5 km of atmosphere and 20 cm of topsoil. The grave danger currently facing these two vital layers of the Earth are well known. Maintaining the health of these layers is of utmost importance if humanity is to continue to prosper into the future.

Visual (Vis) and infrared (NIR) spectroscopy has enjoyed rapid adoption in the field of soil science over the past decade. Many authors have shown ([11], [], [], etc) that various important soil properties (SOC, CEC, %water, pH, N, P, K, Fe, Mg, Mn, etc), can be determined from reflectance spectra of soil samples. Unfortunately though, current spectrographs are not designed for extended deployment in the field. As such high-resolution time-series data and/or maps of large spatial areas are both expensive and time consuming. [euro map]

Astronomers have also been using spectroscopic observations for many decades to determine the composition of “simple” (stars) and complex (galaxies) celestial systems. While high-resolution spectra provide large amounts of information, it was found in the 1950s [strömgren, crawford] that low spectral resolution observations of specific wavelength regions, combined with synthetic spectral models of an object’s composition, were sufficient to accurately determine properties of the objects in question. This family of observation techniques are collectively known as narrow-band photometry, or spectro-photometry.

By adapting spectro-photometric techniques from astronomy to the field of soil science, we expect to be able to massively miniaturise the spectrographs such that they may be deployed en masse and left in-situ for time frames of months to years. Such large scale temporal and spatial data sets of soil parameters would be of immense value to agriculture, environmental monitoring programmes, and basic research. Indeed regional grids of such sensors could enable global maps of soil health, as well as possible financially incentivise (e.g. via carbon markets [NORI, PURO]) a global shift towards regenerative agriculture

Originality and/or risk involved
++++++++++++++++++++++++++++++++
The theoretical foundations for this project already exist in both astronomy and soil science. The originality of this project lies in combining the knowledge bases of these two academic fields to enable the development of miniaturised spectro-photometric sensors capable of repeatedly and non-destructively monitoring in-situ a wide range of ecologically relevant soil properties over long time frames. Additionally we plan to adapt the astrophysical population synthesis modeling technique to generate synthetic spectra of the soil that match the observed photometric data.

The risks associated with the project are described in detail in the “risk assessment” section.

Novelty and (especially) innovative elements
++++++++++++++++++++++++++++++++++++++++++++
Figure 1: Black - the reflection spectrum of a soil sample from [7]. Red - the expected reconstructed spectrum based on 24 spectro-photometric data points (red circles) in the wavelength range [500, 2500]nm. Blue / green gaussian profiles - the emission spectrum of a selection of commercially available visual and near infrared LEDs.

The major innovative elements of this project include:

* Replacing the bulky optics of a conventional spectrograph with a series of LEDs with peak emission wavelengths matched to relevant spectral features. See Figure 1.
* Mimicking low-resolution reflectance spectroscopy by sequentially illuminating soil samples with a series of LEDs with different emission wavelengths.
* Combining the colour-gradients methodology from astronomy with synthetic soil composition spectral modelling (based on stellar population synthesis modelling) to reconstruct the intrinsic spectrum for a soil sample. Soil parameters can be extracted from the reconstructed spectrum by using the methods reported in the literature.
* Determining which combination of LEDs can be used to rapidly and reliably determine singular properties of a soil sample for a given specific application.
* Using internet-of-things enabled devices to transmit in real-time soil property data from in-situ sensors over long time frames.

Transformative potential
++++++++++++++++++++++++
Real-time in-situ soil property and content information gained in a non-destructive and repeatable manner should have a strong transformative effect in many fields, from industrial agriculture, to environmental monitoring programmes, to basic soil science research.

Grids of soil spectro-photometric sensors providing real-time soil property data could enable:

* farmers to profit from carbon markets by providing verifiably data logs of their “carbon farming” activities, thus realising a market driven solution for removing CO2
* Vast improvements in precision agricultural by providing real-time maps of fertiliser and water requirements.
* the potential for global networks to monitor soil health and/or contamination in real-time

The high time-resolution and compactness of LED based spectro-photometers could enable:

* ion exchange processes to be studied on sub-second timescales in the immediate vicinity of the soil-root interface through the use of fibre-optic probes

Ethical, safety, regulatory, sex-specific, and/or gender-related aspects
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
As this project is purely concerned with visual and near infrared spectrometry and data processing of in-house soil samples, there are no ethical, safety-related, or regulatory issues that need to be considered. As there are no extraordinary social interactions foreseen during the course of this project, there are no potential sex-specific or gender-related aspects that need to be considered.

Project implementation
----------------------
Description of the methodological approach
++++++++++++++++++++++++++++++++++++++++++
After the preparation phase (Phase 1) we plan on using an adaptation of the agile test-driven development methodology from software engineering to sequentially cover the growing soil parameter space. This methodology involves achieving a minimum viable result (Phase 2) as soon as possible (i.e. for 3 major soil parameters, e.g. pH, %water, SOC), then iterating over the development pattern (Phase 3) to bring increasingly larger areas of the parameter space (e.g. concentrations of N, P, K, etc) into the final reportable result. We will halt adding further soil parameters approximately 2 months before the end of the project in order for the project results to be collated and presented (Phase 4).

Coherent plan for implementation
++++++++++++++++++++++++++++++++
**Phase 1: Preparation (4 months / 0.167 FTE)**

* Prioritise soil parameters by importance to each field of application (agriculture, environmental monitoring, soil science research), and in descending order by level of independence and strength of influence on the soil reflectance spectrum.
* Compile list of spectral features associated with each parameter.
* Map spectral feature redundancies, search for unique indicators.
* Build the test rack for the spectro-photometric sensor (all electronics without LEDs).

**Phase 2: Minimum viable result (4 months / 0.167 FTE)**

For the 3 most important soil properties (%water, SOC, pH):

* Add LEDs to the sensor breadboard which isolate the relevant spectral features
* For several different soil types from the BOKU research farm and for a representative grid of combinations of the three soil properties:
* Measure the soil property using conventional soil testing methods.
* Measure the reflectance spectrum of the soil samples with both a conventional Vis-NIR spectrograph and the spectro-photometric sensor.
* Determine the degree of correlation between the photometric readout, the intrinsic reflectance spectrum, and the conventionally determined property value.
* Determine the level of influence of the other two parameters on the degree of correlation for each spectral feature associated with each given property.
* Find the most reliable, and where possible, uncontaminated combination of LEDs and spectral features for each soil property.

**Phase 3: Iterations over soil parameters (8 months / 0.333 FTE)**

* Repeat the steps in Phase 2, adding each soil parameter in order of descending priority (e.g: N, P, K, etc…)
* Optimise the test parameter space by being smart about which elemental and ionic concentrations and property combinations are physically realistic. This step is to avoid the parameter space growing exponentially [O(x^N)] with each new parameter added.

**Phase 4: Reporting (2 months / 0.084 FTE)**

The degree of accuracy of spectro-photometric measurements in determining the value of a certain soil parameter is reported at the end of each iteration in phases 2 and 3. Hence this final reporting phase will concentrate primarily on collating the results for publication. Additionally we intend to conduct a retrospective analysis to determine what worked and what did not, as well as what improvements can be made to this technique in any further activities.

A secondary, but very useful result, will be the library of reflectance spectra which will systematically cover the realistic parameter space for all soil parameters included in this project.

Example of how this methodology will work
+++++++++++++++++++++++++++++++++++++++++
Water has several very prominent spectral features (e.g. absorption between 1850-1900nm in Figure 1). For a series of soil samples we will alter the soil moisture content and measure the soil reflectance using both conventional and photometric spectrographs. We will quantify the variation in the spectral features with soil moisture levels. Next we will test organic carbon, which also has well known spectral features. For each of the different moisture levels, we will add increasing amounts of SOC and measure again the soil reflectance with both instruments. The variation in the SOC spectral features will be quantified and modelled with respect to the previous parameter: moisture content. This process will be repeated for additional parameters in order of their importance to the various applications (soil research, industrial agriculture, etc).

Risk assessment and learning potential
--------------------------------------
Risk assessment
+++++++++++++++
High resolution Vis+NIR spectroscopy has already proved to be a viable option for determining ecologically relevant soil properties [11]. The question is whether the same information can be extracted using targeted low resolution spectro-photometric measurements combined with synthetic (or archive) soil spectral models.

Risks to the success of this project include:

* Whether the accuracy of the miniaturised spectro-photometers detectors is sufficient for accurately observing the relative changes in the soil properties. Astronomical photometry regularly achieves accuracies of <0.1% in the relative flux measurements [12]
* Whether the redundancy in spectral features of each of the major soil components can be disentangled with the reduced spectral sampling of a photometer.
* Sensor data in the immediate vicinity of the sensor-soil interface must be taken as representative of the soil volume within a given radius. Random inhomogeneities in soil composition may exceed the systematic uncertainty of the sensors.
* Changing soil conditions (moisture, temperature, irradiation) will introduce a certain level of random fluctuations into the data points. These may or may not be controllable by applying statistical methods to time-series data sets.

Learning potential
------------------
Even in the case of ultimate failure, this project will still provide much useful information to the global soil community. Examples include:

* A library of soil reflectance spectra which systematically and extensively covers the parameter space of the most important soil characteristics
* Which soil parameters can (and cannot) be reliably and repeatedly extracted with certain wavelength features using reflectance spectro-photometry.
* Which spectral feature degeneracies can and cannot be lifted with spectro-photometry

References
----------
[1] Minasny et al, 2017, https://doi.org/10.1016/j.geoderma.2017.01.002
[2] Puro: https://puro.earth/
[3] Nori: https://nori.com/
[4] Milos et al, 2017
[5] Nayak et al, 2019, https://doi.org/10.1016/j.scitotenv.2019.02.125
[6] Kane et al, 2015, Soil_C_review_Kane_Dec_4-final-v4.pdf
[7] Manage et al, 2018, doi:10.2136/sssaj2018.01.0052
[8] Stenberg et al, 2010, https://doi.org/10.1016/S0065-2113(10)07005-7
[9] Bayesian photometric redshift and drop-out photometry: http://www.stsci.edu/~dcoe/BPZ/sedanim.gif
[10] Strömgren, 1956,  https://doi.org/10.1016/0083-6656(56)90060-5
[11] Cheng, 2001,  https://doi.org/10.2136/sssaj2001.652480x
[12] TESS photometry https://heasarc.gsfc.nasa.gov/docs/tess/observing-technical.html
