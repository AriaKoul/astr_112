"""
DESCRIPTION:


"""

# Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

from astropy import units as u
from astropy import constants as c

from astroquery.gaia import Gaia

from astropy.coordinates import SkyCoord
from astroquery.gaia import Gaia

# Getting the data
query_result = pd.read_csv('M67_results.csv')
print(query_result)