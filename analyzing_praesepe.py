"""
DESCRIPTION:
 

"""

### IMPORTS ###
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 



### GETTING THE DATA FROM GAIA ###
query_result = pd.read_csv('praesepe_data.csv') # Outputted 141627 stars (radius = 4 degrees)
print('hello world')