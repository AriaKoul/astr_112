"""
DESCRIPTION:
 

"""

### IMPORTS ###
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 



### GETTING THE DATA FROM GAIA ###
query_result = pd.read_csv('praesepe_data.csv') # Outputted 141627 stars (radius = 4 degrees)


### CREATING A HISTOGRAM FOR THE PARALLAXES ###
parallax_signal = query_result['parallax']
max_parallax = np.max(parallax_signal) # determines what the largest parallax value is in order to define the bins
print(max_parallax) 

bins = np.arange(0.5,10, 0.10) 
plt.hist(parallax_signal,bins)

plt.xlabel('Parallax (mas)')
plt.ylabel('Stars')

plt.title('Parallax Histogram')

plt.show()
# Peak of the histogram had a width from 1.10 mas to 1.20 mas