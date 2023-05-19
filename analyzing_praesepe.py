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
bins_zoomed = np.arange(5, 6, 0.02) # arrangement for zoomed in histogram
plt.hist(parallax_signal,bins_zoomed)
plt.xlabel('Parallax (mas)')
plt.ylabel('Stars')
plt.title('Zoomed in Parallax Histogram (between 5 and 6 mas)')
plt.show()
# Peak of the histogram had a width from 5.28 mas to 5.54 mas: this peak was 13 bins across



### FILTERING THE DATA ###

# We want to filter the stars so that the only stars left in our data set are those that correspond to
# the parallax range we found. So, we want stars that have a parallax between 5.28 mas and 5.54 mas.
query_result = query_result[(query_result['parallax'] >= 5.28) & (query_result['parallax'] <= 5.64)]
print(query_result)

# From 5.24 to 5.54: 1041 stars
# From 5.28 to 5.64: 1105 stars