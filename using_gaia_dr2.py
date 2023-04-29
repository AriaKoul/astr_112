
"""
DESCRIPTION:
This is the first assignment we had using the Gaia Catalog. In this assignment, 
we used the Gaia DR2 Catalog and specified parameters to get data on a bunch of 
stars. 

Below are the parameters we used to gather stars from the entire night sky:
    - A distance less than 50 parsecs
    - A parallax single-to-noise ratio (S/N) greater than 10
    - A S/N greater than 5 in each photometric band (BP, RP, G)
    - An extinction (AG) less than 0.1 mag

Below are the outputs we wanted for each star that fit the above parameters:
    - Source ID
    - Right Ascension
    - Declination 
    - Parallax
    - Parallax Error
    - Mean G Magnitude
    - BP-RP Color
    - Effective Temperature
    - Luminosity

After finding the data using the Gaia Website, I downloaded it as a csv file to 
use in my code. With the data, I made a Hertzsprung Russell Diagram and a Color 
Magnitude Diagram to represent the stars I gathered.

"""


### IMPORTS ###
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

from astropy import units as u
from astropy import constants as c

from astroquery.gaia import Gaia

from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia


### FROM GAIA ARCHIVE WEBSITE ###
query_result = pd.read_csv('gaia_dr2_result.csv')

### This creates a new data frame containing only those stars with valid luminosity values
query_result_filtered = query_result.dropna(subset=['lum_val'])



### PLOTTING THE DATA - HR DIAGRAM ###
luminosities = query_result_filtered['lum_val']
temperatures = query_result_filtered['teff_val']

fig, ax = plt.subplots(figsize=(5,5), dpi=100)

ax.scatter(temperatures,luminosities, s=0.5)

ax.set_xlim(8000,3000)

ax.set_yscale('log')

ax.set_ylabel(r'Luminosity [$L_\odot$]')
ax.set_xlabel('Effective Temperature [K]')

ax.set_title('Hertzsprung-Russel Diagram')

plt.show()



### PLOTTING THE DATA - COLOR MAGNITUDE DIAGRAM ###

# Pull out the color & magnitude values

# Gaia gives apparent magnitude
app_Gmag = query_result_filtered['phot_g_mean_mag']

# The B & R magnitudes are apparent too, but the distance dependence gets cancelled
# out because they are subtracted
bp_rp = query_result_filtered['bp_rp']

# Calculating distance from parallax 
parallax_Signal = query_result_filtered['parallax']
parallax_in_arcsec = parallax_Signal/1000 #convert from milliarcseconds to arcseconds
d = 1/parallax_in_arcsec

# Calculating absolute magnitude using distance 
abs_Gmag = app_Gmag - 5*np.log10(d/10)

# Creating the Color Magnitude Diagram plot 
fig, ax = plt.subplots(figsize=(5,5), dpi=100)

ax.scatter(bp_rp,abs_Gmag, s=0.7)

# The y axis is reversed because smaller magnitude values mean brighter stars,
# and the convention is to put brighter stars at the top
ax.set_ylim(10,2)

ax.set_ylabel(r'Absolute magnitude [Gaia G-band]')
ax.set_xlabel('B-R color [Gaia Bp & Rp bands]')

plt.title('CMD of Gaia stars with d<50pc')

plt.show()
