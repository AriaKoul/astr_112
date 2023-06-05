

### IMPORTS ###
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 


### GETTING THE DATA FROM GAIA ###

# m_44 = pd.read_csv('m_44_data.csv')
# alpha_per = pd.read_csv('alpha_per_data.csv')
# ngc_6774 = pd.read_csv('ngc_6774_data.csv')

def color_magnitude_diagram(query_result):

    query_result_filtered = query_result.dropna(subset=['phot_g_mean_mag'])
    query_result_filtered = query_result.dropna(subset=['bp_rp'])

    # Pull out the color & magnitude values from Gaia
    app_Gmag = query_result_filtered['phot_g_mean_mag']
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

    # The y axis is reversed because smaller magnitude values mean brighter stars,and the convention is to put brighter stars at the top
    ax.set_ylim(16, -4)

    ax.set_ylabel(r'Absolute magnitude [Gaia G-band]')
    ax.set_xlabel('B-R color [Gaia Bp & Rp bands]')

    plt.title('Color Magnitude Diagram of Stars')

color_magnitude_diagram(pd.read_csv('M44_data.csv'))
color_magnitude_diagram(pd.read_csv('alpha_per_data.csv'))

plt.legend()
plt.show()



