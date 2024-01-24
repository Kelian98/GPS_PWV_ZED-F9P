### GNSS format

#### RINEX measurement files

This standard gathers the GNSS observations collected by a receiver. The file is divided clearly into two different sections: the header section and the observables section. While in the header global information is given for the entire file, the observables section contains the code and carrier measurements, among others, stored by epoch.

Files are kept to 81-character lines.

#### RINEX navigation files

The standard navigation messages broadcast by the GNSS satellites discussed here can vary slightly from one satellite system to another. For example, while the GPS navigation RINEX contains pseudo-Keplerian elements that permit the calculation of the satellite’s position, Glonass navigation RINEX contains the satellite’s position, velocity and Sun and Moon acceleration in order to integrate the satellite orbits using the Runge– Kutta numerical method.

#### Global Ionospheric Map files : IONEX

Using a GNSS tracking network it is possible to extract information about the TEC of the ionosphere on a global scale. The IONEX format is a welldefined standard used to exchange ionospheric maps. It follows the same philosophy as the RINEX format, even when the files are organised into a header and a data section where the maps are allocated.

#### RINEX clock files

The standard files provide station and satellite clock data. Four types of information are given in this format: data analysis results for receiver and satellite clocks derived from a set of network receivers and satellites with respect to a reference clock; broadcast satellite clock monitoring;, discontinuity measurements; and calibration(s) of single GNSS receivers.

#### APC files : ANTEX

These standard files in ANTEX contain satellite and receiver antenna corrections. Satellite data include satellite and block-specific PCO. Receiver data include elevation and azimuth-dependent corrections for combinations of antennas and radomes.

#### Precise orbit and clock files : SP3

Precise orbital data (satellite position and velocity), the associated satellite clock corrections, orbit accuracy exponents, correlation information between satellite coordinates and satellite clock are available in this format.

**Precise clocks for GPS satellites can be found on the International GNSS Service (IGS) server https://igs.org/products/#orbits_clocks**

The IGS Analysis Centers (ACs) submit GNSS satellite orbit and satellite and station clock solutions, as well as Earth rotation parameters (ERPs), to the global data centers on sub-daily, daily or weekly schedules. These solutions are combined to form the official IGS products. The IGS orbit, clock and ERP products include:

- IGS ultra-rapid orbits and ERPs: useful for real-time and near-real-time applications, provided four times per day (every six hours). They consist of 24 hours of observed and 24 hours of predicted combined satellite orbits (and ERPs).
- IGS rapid orbits, clocks and ERPs: daily combined solutions available approximately 17 hours after the end of the previous UTC day.
- IGS final orbits, clocks and ERPs: considered the highest quality and the most consistent IGS products, include daily combined satellite orbits. The IGS final ERPs are derived from the terrestrial frame combinations (see https://igs.org/products#terrestrial_frame).

Combined solutions are also provided as part of each IGS reprocessing campaign.

The current orbit and clock combination strategy is described in [Griffiths (2019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6394744/). Work on multi-GNSS combinations is underway. The third IGS reprocessing campaign consisted for the first time of GPS, GALILEO and GLONASS combined solutions ([Masoumi & Moore, 2021](https://files.igs.org/pub/resource/pubs/workshop/2021/04-Masoumi.pdf)) and [Geng et al. (2021)](https://files.igs.org/pub/resource/pubs/workshop/2021/06-Geng.pdf?_ga=2.101966145.1589282169.1675637909-974386736.1661838621&_gl=1*19t3jsy*_ga*OTc0Mzg2NzM2LjE2NjE4Mzg2MjE.*_ga_Z5RH7R682C*MTY3NTY0NzQ5Ny4xMzkuMS4xNjc1NjQ3NTI2LjMxLjAuMA..). Demonstration multi-GNSS combinations are soon to be published on an operational basis, and a multi-GNSS task force group is currently running with the aim to eventually provide fully multi-GNSS combinations.

**Stable clocks with a sampling rate of 30 sec or higher can be interpolated with a first-order polynomial to a few centimetres of accuracy. Clocks with a lower sampling rate should not be interpolated, because clocks evolve as random walk processes.**



## Tropospheric Products

https://igs.org/products/#troposphere

IGS associate analysis centers generate troposphere products from ground-based GNSS data. These products include five-minute estimates of zenith path delay (ZPD) and north and east troposphere gradient components. Data are available in daily files by site for over 350 GNSS stations in the IGS network. Measurements of surface pressure and temperature at GNSS sites allow the extraction of precipitable water vapor from the total zenith path delay. Final troposphere estimates for over 350 stations in the IGS network. The troposphere products utilize the IGS final satellite, orbit, and EOP products and are therefore available approximately three weeks following the observation day. Troposphere products are available in a standard, [IGS format](https://files.igs.org/pub/data/format/sinex_tropo.txt).

Since the inception of the troposphere product, three analysis groups (GFZ, JPL, and currently USNO) have generated the IGS combination solution each using different methodologies. Therefore, the resulting file types have changed through the years. The current product consists of files containing daily ZPD estimates for selected sites in the IGS network. The original product consisted of one file per site per GPS week.

