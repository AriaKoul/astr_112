
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
use in my code.

"""


# IMPORTS
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

from astropy import units as u
from astropy import constants as c

from astroquery.gaia import Gaia

from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia


### FROM GAIA ARCHIVE WEBSITE
query_result = pd.read_csv('gaia_dr2_result.csv')

### This creates a new data frame containing only those stars with valid luminosity values
query_result_filtered = query_result.dropna(subset=['lum_val'])

### Plotting the Data - HR Diagram
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




### Plotting the data - Color Magnitude Diagram
g_mag = query_result_filtered['phot_g_mean_mag']
bp_rp_color = query_result_filtered['bp_rp']

fig, ax = plt.subplots(figsize=(5,5), dpi=100)

ax.scatter(g_mag,bp_rp_color, s=0.5)

ax.set_ylim(2.5, 0, 0.25)

ax.set_ylabel(r'Absolute G Magnitude')
ax.set_xlabel('BP RP Color')

ax.set_title('Color Magnitude Diagram')

plt.show()

