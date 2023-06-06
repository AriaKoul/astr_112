

### IMPORTS ###
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 



### PLOTTING COLOR MAGNITUDE DIAGRAM FOR ALL FOUR CLUSTERS ###

# I filtered the data and created the following csv files, so that the color magnitude diagram at 
# the end of part (a) was less chaotic and more clear. 

'''
csv_files = ['alpha_per_filtered.csv', 'NGC188_filtered.csv', 'NGC6774_filtered.csv', 'M44_filtered.csv']

def color_magnitude_diagram(csv_files):
    for file in csv_files:
        query_result = pd.read_csv(file)

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
        # fig, ax = plt.subplots(figsize=(5,5), dpi=100)
        # ax.scatter(bp_rp,abs_Gmag, label = file)

        plt.scatter(bp_rp, abs_Gmag, s = 0.5, label = file.split('_filtered.csv')[0])

    # The y axis is reversed because smaller magnitude values mean brighter stars,and the convention is to put brighter stars at the top
    plt.ylim(16, -4)

    plt.ylabel(r'Absolute magnitude [Gaia G-band]')
    plt.xlabel('B-R color [Gaia Bp & Rp bands]')

    plt.title('Color Magnitude Diagram of Stars in the Alpha-Per, NGC 188, NGC 6774, and M44 Clusters')

    plt.legend()
    plt.show()

print(color_magnitude_diagram(csv_files))

'''

### USING THE ISOCHRONES ###
iso = pd.read_csv('iso.csv')

# Below is the work I used to create a new csv file with the BP - RP color included
    # bp_rp = iso['BPmag'] - iso['RPmag']
    # iso['bp_rp'] = bp_rp
    # new_csv_file_path = "iso_with_bp_rp.csv"
    # iso.to_csv(new_csv_file_path, index=False)

iso_with_bp_rp = pd.read_csv('iso_with_bp_rp.csv')

# Filtering for each specific age
iso_filtered_1 = iso_with_bp_rp[(iso_with_bp_rp['logAge   '] == 7.50000)]
iso_filtered_2 = iso_with_bp_rp[(iso_with_bp_rp['logAge   '] == 8.50000)]
iso_filtered_3 = iso_with_bp_rp[(iso_with_bp_rp['logAge   '] == 9.50000)]

# Plotting the Color Magnitude Diagram for these isochrones
isochrones = [iso_filtered_1, iso_filtered_1, iso_filtered_3]

def color_magnitude_diagram_iso(isochrones):
    for isochrone in isochrones:

        # Pull out the color & magnitude values from Gaia
        app_Gmag = isochrone['Gmag']
        bp_rp = isochrone['bp_rp']

        # # Calculating distance from parallax 
        # parallax_Signal = query_result_filtered['parallax']
        # parallax_in_arcsec = parallax_Signal/1000 #convert from milliarcseconds to arcseconds
        # d = 1/parallax_in_arcsec

        # # Calculating absolute magnitude using distance 
        # abs_Gmag = app_Gmag - 5*np.log10(d/10)

        # # Creating the Color Magnitude Diagram plot 
        # # fig, ax = plt.subplots(figsize=(5,5), dpi=100)
        # # ax.scatter(bp_rp,abs_Gmag, label = file)

        plt.scatter(bp_rp, app_Gmag, s = 0.5, label = 'isochrone')

    # The y axis is reversed because smaller magnitude values mean brighter stars,and the convention is to put brighter stars at the top
    plt.ylim(16, -4)

    plt.ylabel(r'Absolute magnitude [Gaia G-band]')
    plt.xlabel('B-R color [Gaia Bp & Rp bands]')

    plt.title('Color Magnitude Diagram of Three Isochrones')

    plt.legend()
    plt.show()

print(color_magnitude_diagram_iso(isochrones))
