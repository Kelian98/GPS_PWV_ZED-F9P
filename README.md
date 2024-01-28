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


## Current limitations
* Using *rapid* products and not *final products*
* GNSS receiver and antenna installed on the side wall of building. Therefore, low number of satellites with high SNR are available. For example, GLab cannot provide solutions.
* Not enough timeseries data for convergence (at least 24 hours required in static mode)
* Weather data is coming from nearby weather station in the city through meteostat queries. Non-local measurements of atmospheric pressure $P_{atm}$ might affect the measurements.
* Solution for every measurement epoch required. No decimation.
* Elevation mask needs to be set around 10 degrees for improved SNR (also called cut-off angle)
* Ocean Tide Loading (OTL) file obtained with the GOT00.2 model needs to be input for improved accuracy


## Software
* [pyubx2](https://github.com/semuconsulting/pyubx2) : Low-level Python library to manage u-blox devices and data
* [pygnssutils](https://github.com/semuconsulting/pygnssutils): High-level Python library to acquire data from CLI
* [pygpsclient](https://github.com/semuconsulting/PyGPSClient): High-level Python library to acquire data from GUI
* [RTKLIB](https://github.com/rinex20/RTKLIB-demo5): full software to convert, process and analyze GNSS data
* [Teqc](https://www.unavco.org/software/data-processing/teqc/teqc.html): tools to convert, process and analyze GNSS data
* [GFZRNX](https://gnss.gfz-potsdam.de/services/gfzrnx): toolbox to manipulate RINEX files


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
* Need to convert raw UBX file to RINEX file in 2.11 version format in order to be compatible with GFZRNX and GLab concurrently.
* Sample rate of 4Hz (250ms) produces too large data files : 1 hour in RINEX ~ 70 MB => 1.7 GB/day.

### Convert raw UBX file to RINEX format

Need to install : `sudo apt-get install convbin`

```bash
convbin -od -os -oi -ot -f 5 filename.ubx -r ubx -v 2.11
-v ver       rinex version [3.04]
-od          include doppler frequency in rinex obs [on]
-os          include snr in rinex obs [on]
-oi          include iono correction in rinex nav header [off]
-ot          include time correction in rinex nav header [off]
-r format    log format type
rtcm2= RTCM 2
rtcm3= RTCM 3
nov  = NovAtel OEM/4/V/6/7,OEMStar
oem3 = NovAtel OEM3
ubx  = ublox LEA-4T/5T/6T/7T/M8T/F9
ss2  = NovAtel Superstar II
hemis= Hemisphere Eclipse/Crescent
stq  = SkyTraq S1315F
javad= Javad GREIS
nvs  = NVS NV08C BINR
binex= BINEX
rt17 = Trimble RT17
sbf  = Septentrio SBF
rinex= RINEX

# Example
(base) sommer@portable-sommer:~/Documents/PWV/data$ convbin -od -os -oi -ot -f 5 2024-01-24T22:16:08.453071.ubx -r ubx -v 2.11
input file  : 2024-01-24T22:16:08.453071.ubx (u-blox UBX)
->rinex obs : 2024-01-24T22:16:08.453071.obs
->rinex nav : 2024-01-24T22:16:08.453071.nav
->rinex gnav: 2024-01-24T22:16:08.453071.gnav
->rinex hnav: 2024-01-24T22:16:08.453071.hnav
->rinex qnav: 2024-01-24T22:16:08.453071.qnav
->rinex lnav: 2024-01-24T22:16:08.453071.lnav
->rinex cnav: 2024-01-24T22:16:08.453071.cnav
->rinex inav: 2024-01-24T22:16:08.453071.inav
->sbas log  : 2024-01-24T22:16:08.453071.sbs

scanning: 2024/01/27 19:05:44 GRES
2024/01/24 22:16:28-01/27 19:05:44: O=991027 N=498 G=1186 H=2594 L=1895 S=494976 E=8
```

