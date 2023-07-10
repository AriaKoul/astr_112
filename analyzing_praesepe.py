"""
DESCRIPTION:
In this assignment, I am analyzing the M44 (aka Praesepe Cluster, aka Beehive Cluster)
in the Cancer constellation. From the Gaia DR2 catalog, I used specific parameters to
get data on a bunch of stars.

Below are the parameters I used to gather stars from the entire night sky. I knew that the Praesepe
Cluster takes up a large portion of the night sky so I made my radius larger than usual. Also,
I knew that Praesepe is a nearby cluster, so its parallax value would have than about 
0.5 milliarcseconds (mas). Here are the parameters:
    - Radius = 4 degrees
    - Parallax >= 0.5 mas (which corresponds to a distance, d less than 2000 parsecs)

Below are the outputs I needed for each star to analyze the data.
    - Source ID
    - Parallax
    - Right Ascension (RA)
    - Declination (DEC)
    - Proper Motion in RA (pmra)
    - Proper Motion in DEC (pmdec)
    - Mean G Magnitude
    - BP-RP Color 

After finding the data using the Gaia website, I downloaded it as a csv file to use in my code.
With the data, I first made a histogram of the parallaxes. This helped me find the approximate range
of parallaxes for the stars in M67, and thus the approximate distance range for the whole cluster.
Then, I found the approximate ranges for the RA, DEC, pmra, and pmdec for all the stars in the cluster.
This helped me filter the stars in the initial Gaia query so that, in the end, the only stars remaining
in the data set were those from the Praesepe Cluster. At the end of this assignment, I made a Color
Magnitude Diagram to represent the stars in the cluster. 

NOTE: Thank you to Thummim Merkuria for their help with the code.


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
print(max_parallax) # max parallax was 92.22 mas 

# Below is the code for the entire parallax histogram
bins = np.arange(0, 8, 0.05) 
plt.hist(parallax_signal,bins)
plt.xlabel('Parallax (mas)')
plt.ylabel('Stars')
plt.title('Parallax Histogram for the Praesepe Cluster')
plt.show()

# # Below is the code for the parallax histogram zoomed into the parallaxes that the Praesepe Cluster might correspond to
bins_zoomed = np.arange(5, 6, 0.02) 
plt.hist(parallax_signal,bins_zoomed)
plt.xlabel('Parallax (mas)')
plt.ylabel('Stars')
plt.title('Zoomed in Parallax Histogram for the Praesepe Cluster (between 5 and 6 mas)')
plt.show()
# Peak of the histogram had a width from 5.28 mas to 5.64 mas: this peak was 18 bins across



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

ax.set_ylabel('Proper Motion in Right Ascension, RA (mas/yr)')
ax.set_xlabel('Proper Motion in Declination, DEC (mas/yr)')

plt.title('Proper Motion in RA vs. Proper Motion in DEC')

plt.show()



### FILTERING THE DATA FOR PROPER MOTION AND PLOTTING PROPER MOTION AGAIN ###

query_result_filtered_2 = query_result_filtered[(query_result_filtered['pmdec'] >= -18.0) & (query_result_filtered['pmdec'] <= -7.5)
                                                & (query_result_filtered['pmra'] >= -45.5) & (query_result_filtered['pmra'] <= -27.0)]



pm_RA_filtered = query_result_filtered_2['pmra']
pm_DEC_filtered = query_result_filtered_2['pmdec']

fig, ax = plt.subplots(figsize=(5,5), dpi=100)

ax.scatter(pm_DEC_filtered,pm_RA_filtered, s=0.3)

ax.set_ylabel('Proper Motion in Right Ascension, RA (mas/yr)')
ax.set_xlabel('Proper Motion in Declination, DEC (mas/yr)')

plt.title("Proper Motion in RA vs. Proper Motion in DEC (zoomed in)")

plt.show()



### PLOTTING RA vs. DEC FOR INITIAL QUERY (UNFILTERED DATA) ###

condition = ((query_result['parallax'].between(5.28, 5.64)) & (query_result['pmdec'].between(-18.0, -7.5)) 
             & (query_result['pmra'].between(-45.5, -27.0)))
selected_points = query_result[condition]


fig, ax = plt.subplots(figsize=(5,5), dpi=100)
ax.scatter(query_result['dec'], query_result['ra'], s = 0.3, color = 'blue', label = 'All stars')
ax.scatter(selected_points['dec'], selected_points['ra'], s = 0.4, color = 'red', label = 'Selected stars')

ax.set_ylabel('Right Ascension (degrees)')
ax.set_xlabel('Declination (degrees)')
plt.title('Right Ascension vs. Declination')
plt.legend()
plt.show()


### FILTERING THE DATA FOR RA AND DEC ### 

query_result_filtered_3 = query_result_filtered_2[(query_result_filtered_2['dec'] >= 18.0) & (query_result_filtered_2['dec'] <= 21.5)
                                                & (query_result_filtered_2['ra'] >= 128.0) & (query_result_filtered_2['ra'] <= 132.0)]
# 534 stars were left after filtering all the data 


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
