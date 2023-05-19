"""
DESCRIPTION:
 

"""

### IMPORTS ###
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 



### GETTING THE DATA FROM GAIA ###
query_result = pd.read_csv('praesepe_data.csv') # Outputted 141627 stars (using radius = 4 degrees, parallax >= 0.5)


### CREATING A HISTOGRAM FOR THE PARALLAXES ###
parallax_signal = query_result['parallax']
max_parallax = np.max(parallax_signal) # determines what the largest parallax value is in order to define the bins
# print(max_parallax) # max parallax was 92.22 mas 

# Below is the code for the entire parallax histogram
# bins = np.arange(0, 8, 0.05) 
# plt.hist(parallax_signal,bins)
# plt.xlabel('Parallax (mas)')
# plt.ylabel('Stars')
# plt.title('Parallax Histogram')
# plt.show()

# # Below is the code for the parallax histogram zoomed into the parallaxes that the Praesepe Cluster might correspond to
# bins_zoomed = np.arange(5, 6, 0.02) # arrangement for zoomed in histogram
# plt.hist(parallax_signal,bins_zoomed)
# plt.xlabel('Parallax (mas)')
# plt.ylabel('Stars')
# plt.title('Zoomed in Parallax Histogram (between 5 and 6 mas)')
# plt.show()
# Peak of the histogram had a width from 5.28 mas to 5.54 mas: this peak was 13 bins across



### FILTERING THE DATA FOR PARALLAX ###

# We want to filter the stars so that the only stars left in our data set are those that correspond to
# the parallax range we found. So, we want stars that have a parallax between 5.28 mas and 5.54 mas.
query_result_filtered = query_result[(query_result['parallax'] >= 5.28) & (query_result['parallax'] <= 5.64)]

# From 5.24 to 5.54: 1041 stars
# From 5.28 to 5.64: 1105 stars



### PLOTTING THE PROPER MOTION ###
# In this section, we want to plot proper motion in RA versus proper motion in DEC
# pm_RA = query_result_filtered['pmra']
# pm_DEC = query_result_filtered['pmdec']

# fig, ax = plt.subplots(figsize=(6,6), dpi=100)

# ax.scatter(pm_DEC,pm_RA, s=0.3)

# ax.set_ylabel('Proper Motion in Right Ascension (RA)')
# ax.set_xlabel('Proper Motion in Declination (DEC)')

# plt.title('Proper Motion in RA vs. Proper Motion in DEC')

# plt.show()



### FILTERING THE DATA FOR PROPER MOTION AND PLOTTING PROPER MOTION AGAIN ###

query_result_filtered_2 = query_result_filtered[(query_result_filtered['pmdec'] >= -18.0) & (query_result_filtered['pmdec'] <= -7.5)
                                                & (query_result_filtered['pmra'] >= -45.5) & (query_result_filtered['pmra'] <= -27.0)]

pm_RA_filtered = query_result_filtered_2['pmra']
pm_DEC_filtered = query_result_filtered_2['pmdec']

fig, ax = plt.subplots(figsize=(6,6), dpi=100)

ax.scatter(pm_DEC_filtered,pm_RA_filtered, s=0.3)

ax.set_ylabel('Proper Motion in Right Ascension (RA)')
ax.set_xlabel('Proper Motion in Declination (DEC)')

plt.title('Proper Motion in RA vs. Proper Motion in DEC')

plt.show()