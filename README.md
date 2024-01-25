# GPS_PWV_ZED-F9P
Code to get required data for PWV estimation from [u-blox ZED-F9P GNSS receiver](https://gnss.store/zed-f9p-gnss-modules/99-elt0087.html) with [multi-band L1/L2/L5 GPS, G1/G2/G3 GLONASS, B1/B2/B3 antenna](https://gnss.store/gnss-rtk-multiband-antennas/140-elt0123.html) instruments. Raw UXB data is later converted with [RTKLIB](https://github.com/rinex20/RTKLIB-demo5) `convbin` tool. Finally, ZTD is calculated through PPP computations with additional software.

## Todo
- [ ] Check IGN report for file lacking n# observations with > 5 satellites
- [ ] Test the gLAB with sample data (from IGS base stations maybe ?) following tutorial PDF
- [x] Setup the automated collection of data hardware with Raspberry Pi
- [x] Implement : https://github.com/semuconsulting/pygnssutils/blob/main/examples/gnssapp.py
- [x] Collect new data for > 1 day continuous with new upgraded code (UBX-RXM-SFRBX)
- [x] Acquisition code with queue, etc
- [x] Proper downloading of reference IGS files (CLK and SP3) for futher PPP processing
- [x] Check conversion of raw UBX files with RTKLIB


## Software
* pyubx2 : https://github.com/semuconsulting/pyubx2
* pygnssutils : https://github.com/semuconsulting/pygnssutils
* pygpsclient : https://github.com/semuconsulting/PyGPSClient
* RTKLIB : https://github.com/rinex20/RTKLIB-demo5
* Teqc : https://www.unavco.org/software/data-processing/teqc/teqc.html


## Tools for PPP

* IGS Data Products : https://igs.org/products-access/
* GLab : https://gage.upc.edu/en/learning-materials/software-tools/glab-tool-suite
* CSRS-PPP : https://webapp.csrs-scrs.nrcan-rncan.gc.ca/geod/tools-outils/ppp.php?locale=en

## Papers
* Real-time retrieval of precipitable water vapor from GPS precise point positioning : https://doi.org/10.1002/2014JD021486
* Precipitable Water Vapor Measurement using GNSS Data in the Atacama Desert for Millimeter and Submillimeter Astronomical Observations : https://arxiv.org/abs/2308.12632
* Analysing the Zenith Tropospheric Delay Estimates in On-line Precise Point Positioning (PPP) Services and PPP Software Packages : https://doi.org/10.3390/s18020580


## Others
* Tropospheric Delay : https://gssc.esa.int/navipedia/index.php/Tropospheric_Delay
* u-blox ZED-F9P interface description : https://content.u-blox.com/sites/default/files/documents/u-blox-F9-HPG-1.32_InterfaceDescription_UBX-22008968.pdf


## Notes
* The ZED-F9P doesn’t output RINEX data, you’d need to save a file containing the UBX-RXM-RAWX and UBX-RXM-SFRBX messages. Then, these binary files need to be converted into RINEX files with utilities from RTKLB (RTKCONV for GUI or convbin for CLI)