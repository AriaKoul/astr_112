"""
DESCRIPTION:
In this assignment, we are analyzing the M67 cluster, which is a nearby open cluster
in the Cancer constellation. From the Gaia DR2 catalog, we used specified parameters to 
get data on a bunch of stars.

Below are the parameters we used to gather stars from the entire night sky. Each 
parameter is similar to a property we know about the M67 cluster, so the stars we 
gathered are all either in M67 or near it:
    - Radius of roughly 40 arcminutes (so the star is in the spatial extent of M67)
    - Coordinates (approximately): RA = 132.82, DEC = 11.82 (so the star is in the direction
        of M67)
    - Within a distance of less than 2000 parsecs

Below are the outputs we needed for each star to analyze the data:
    - Source ID
    - Parallax
    - Mean G Magnitude
    - BP-RP Color

After finding the data using the Gaia Website, I downloaded it as a csv file to use in my 
code. With the data, I made a histogram of the parallaxes. This helped me find the 
approximate parallax, and thus the approximate distances, of the stars in M67. I also made a 
Color Magnitude Diagram to represent the stars that are in M67. 

"""

### IMPORTS ###
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 



### GETTING THE DATA FROM GAIA ###
query_result = pd.read_csv('M67_data.csv') # Outputted 5546 stars 



### CREATING A HISTOGRAM FOR THE PARALLAXES ###
parallax_signal = query_result['parallax']
max_parallax = np.max(parallax_signal) # determines what the largest parallax value is in order to define the bins
print(max_parallax) # found to be 22.04

bins = np.arange(0.5,8,0.10) #define bins with the first one at SNR=10 & going up to 4000 in steps of 50
plt.hist(parallax_signal,bins)

plt.xlabel('Parallax (mas)')
plt.ylabel('Stars')

plt.title('Parallax Histogram')

plt.show()
# Peak of the histogram had a width from 1.10 mas to 1.20 mas



### FILTERING THE DATA ###

# In making a Color Magnitude Diagram, we only want the stars that have a parallax
# value within the range found in the histogram. That is, we want stars that have
# a parallax between 1.10 mas and 1.20 mas only.
query_result = query_result[(query_result['parallax'] >= 1.10) & (query_result['parallax'] <= 1.20)]


# Some rows had invalid BP - RP values. Below, I filtered the data to get only the
# stars with valid BP - RP values.
query_result_filtered = query_result.dropna(subset=['bp_rp'])

# After both filters, there were 855 stars left in the data set




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
ax.set_ylim(12, -5)

ax.set_ylabel(r'Absolute magnitude [Gaia G-band]')
ax.set_xlabel('B-R color [Gaia Bp & Rp bands]')

plt.title('Color Magnitude Diagram of Stars in the M67 Cluster')

plt.show()



