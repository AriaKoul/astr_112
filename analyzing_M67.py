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

# Some rows had invalid effective temperature values and others had invalid AG
# extinction values




