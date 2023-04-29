"""
DESCRIPTION:


"""

### IMPORTS
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

from astropy import units as u
from astropy import constants as c

from astroquery.gaia import Gaia

from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

### GETTING THE DATA FROM GAIA
query_result = pd.read_csv('M67_results.csv') # Outputted 5546 stars 


### CREATING A HISTOGRAM FOR THE PARALLAXES ###
parallax_signal = query_result['parallax']
max_parallax = np.max(parallax_signal) # determines what the largest parallax value is in order to define the bins
print(max_parallax) # found to be 22.04

bins = np.arange(0.5,8,0.25) #define bins with the first one at SNR=10 & going up to 4000 in steps of 50
plt.hist(parallax_signal,bins)

plt.xlabel('Parallax (mas)')
plt.ylabel('Stars')

plt.title('Parallax Histogram')

plt.show()




### ADJUSTING THE DATA ###
# Some rows had invalid BP - RP values. Below, I filtered the data to get only the
# stars with valid BP - RP values.

query_result_filtered = query_result.dropna(subset=['bp_rp'])




