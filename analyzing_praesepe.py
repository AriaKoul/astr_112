"""
DESCRIPTION:
 

"""

### IMPORTS ###
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 



### GETTING THE DATA FROM GAIA ###
query_result = pd.read_csv('praesepe_data.csv') # Outputted 141627 stars (using radius = 4 degrees, parallax >= 0.5)

'''
### CREATING A HISTOGRAM FOR THE PARALLAXES ###
parallax_signal = query_result['parallax']
max_parallax = np.max(parallax_signal) # determines what the largest parallax value is in order to define the bins
print(max_parallax) # max parallax was 92.22 mas 

# Below is the code for the entire parallax histogram
bins = np.arange(0, 8, 0.05) 
plt.hist(parallax_signal,bins)
plt.xlabel('Parallax (mas)')
plt.ylabel('Stars')
plt.title('Parallax Histogram for the Praesepe Cluster')
plt.show()

# # Below is the code for the parallax histogram zoomed into the parallaxes that the Praesepe Cluster might correspond to
bins_zoomed = np.arange(5, 6, 0.02) # arrangement for zoomed in histogram
plt.hist(parallax_signal,bins_zoomed)
plt.xlabel('Parallax (mas)')
plt.ylabel('Stars')
plt.title('Zoomed in Parallax Histogram for the Praesepe Cluster (between 5 and 6 mas)')
plt.show()
# Peak of the histogram had a width from 5.28 mas to 5.54 mas: this peak was 13 bins across
'''


### FILTERING THE DATA FOR PARALLAX ###

# We want to filter the stars so that the only stars left in our data set are those that correspond to
# the parallax range we found. So, we want stars that have a parallax between 5.28 mas and 5.54 mas.
query_result_filtered = query_result[(query_result['parallax'] >= 5.28) & (query_result['parallax'] <= 5.64)]
# After filtering the data for parallaxes, the remaining data was only 1105 stars. 


### PLOTTING THE PROPER MOTION ###
# In this section, we want to plot proper motion in RA versus proper motion in DEC
pm_RA = query_result_filtered['pmra']
pm_DEC = query_result_filtered['pmdec']

fig, ax = plt.subplots(figsize=(6,6), dpi=100)

ax.scatter(pm_DEC,pm_RA, s=0.3)

ax.set_ylabel('Proper Motion in Right Ascension (RA)')
ax.set_xlabel('Proper Motion in Declination (DEC)')

plt.title('Proper Motion in RA vs. Proper Motion in DEC')

plt.show()



### FILTERING THE DATA FOR PROPER MOTION AND PLOTTING PROPER MOTION AGAIN ###

query_result_filtered_2 = query_result_filtered[(query_result_filtered['pmdec'] >= -18.0) & (query_result_filtered['pmdec'] <= -7.5)
                                                & (query_result_filtered['pmra'] >= -45.5) & (query_result_filtered['pmra'] <= -27.0)]



pm_RA_filtered = query_result_filtered_2['pmra']
pm_DEC_filtered = query_result_filtered_2['pmdec']

fig, ax = plt.subplots(figsize=(5,5), dpi=100)

ax.scatter(pm_DEC_filtered,pm_RA_filtered, s=0.3)

ax.set_ylabel('Proper Motion in Right Ascension (RA)')
ax.set_xlabel('Proper Motion in Declination (DEC)')

plt.title("Proper Motion in RA vs. Proper Motion in DEC (zoomed in)")

plt.show()


'''
### PLOTTING RA vs. DEC FOR INITIAL QUERY (UNFILTERED DATA) ###

condition = ((query_result['parallax'].between(5.28, 5.64)) & (query_result['pmdec'].between(-18.0, -7.5)) 
             & (query_result['pmra'].between(-45.5, -27.0)))
selected_points = query_result[condition]


fig, ax = plt.subplots(figsize=(5,5), dpi=100)
ax.scatter(query_result['dec'], query_result['ra'], s = 0.3, color = 'blue', label = 'All points')
ax.scatter(selected_points['dec'], selected_points['ra'], s = 0.4, color = 'red', label = 'Selected Points')

ax.set_ylabel('Right Ascension')
ax.set_xlabel('Declination')
plt.title('Right Ascension vs. Declination')
plt.legend()
plt.show()
'''

### FILTERING THE DATA FOR RA AND DEC ### 

query_result_filtered_3 = query_result_filtered_2[(query_result_filtered_2['dec'] >= 18.0) & (query_result_filtered_2['dec'] <= 21.5)
                                                & (query_result_filtered_2['ra'] >= 128.0) & (query_result_filtered_2['ra'] <= 132.0)]
print(query_result_filtered_3)

### PLOTTING COLOR MAGNITUDE DIAGRAM ###

# Pull out the color & magnitude values from Gaia
app_Gmag = query_result_filtered_3['phot_g_mean_mag']
bp_rp = query_result_filtered_3['bp_rp']

# Calculating distance from parallax 
parallax_Signal = query_result_filtered_3['parallax']
parallax_in_arcsec = parallax_Signal/1000 #convert from milliarcseconds to arcseconds
d = 1/parallax_in_arcsec

# Calculating absolute magnitude using distance 
abs_Gmag = app_Gmag - 5*np.log10(d/10)

# Creating the Color Magnitude Diagram plot 
fig, ax = plt.subplots(figsize=(5,5), dpi=100)
ax.scatter(bp_rp,abs_Gmag, s=0.7)

# The y axis is reversed because smaller magnitude values mean brighter stars,and the convention is to put brighter stars at the top
ax.set_ylim(16, -4)

ax.set_ylabel(r'Absolute magnitude [Gaia G-band]')
ax.set_xlabel('B-R color [Gaia Bp & Rp bands]')

plt.title('Color Magnitude Diagram of Stars in the Praesepe Cluster')

plt.show()



