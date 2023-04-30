"""
DESCRIPTION:


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



### GETTING THE DATA FROM GAIA ###
query_result = pd.read_csv('M67_data.csv') # Outputted 5546 stars 



### CREATING A HISTOGRAM FOR THE PARALLAXES ###
# parallax_signal = query_result['parallax']
# max_parallax = np.max(parallax_signal) # determines what the largest parallax value is in order to define the bins
# print(max_parallax) # found to be 22.04

# bins = np.arange(0.5,8,0.10) #define bins with the first one at SNR=10 & going up to 4000 in steps of 50
# plt.hist(parallax_signal,bins)

# plt.xlabel('Parallax (mas)')
# plt.ylabel('Stars')

# plt.title('Parallax Histogram')

# plt.show()

# Found that most of the stars have a parallax between 1.00 and 1.25 mas



### FINDING DISTANCE OF M67 CLUSTER USING PARALLAX ###

# All parallax values below are in arcseconds and all distance values are in parsecs.
'''parallax_lower = 0.0010
distance_lower = 1/parallax_lower
parallax_upper = 0.00120
distance_upper = 1/parallax_upper

avg_parallax = 0.00115
approx_dist = 1/avg_parallax
'''


### ADJUSTING THE DATA ###

# In making a Color Magnitude Diagram, we only want the stars that have a parallax
# value within the range found in the histogram. That is, we want stars that have
# a parallax between 1.10 mas and 1.20 mas only.
query_result = query_result[(query_result['parallax'] >= 1.10) & (query_result['parallax'] <= 1.20)]


# Some rows had invalid BP - RP values. Below, I filtered the data to get only the
# stars with valid BP - RP values.
query_result_filtered = query_result.dropna(subset=['bp_rp'])
print(query_result_filtered)


### PLOTTING THE DATA - COLOR MAGNITUDE DIAGRAM ###



