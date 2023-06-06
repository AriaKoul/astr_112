

### IMPORTS ###
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 



### PLOTTING COLOR MAGNITUDE DIAGRAM FOR ALL FOUR CLUSTERS ###

# I filtered the data and created the following csv files, so that the color magnitude diagram at 
# the end of part (a) was less chaotic and more clear. 

csv_files = ['alpha_per_filtered.csv', 'NGC188_filtered.csv', 'NGC6774_filtered.csv', 'M44_filtered.csv']
names = ['Alpha Persei, NGC 188, NGC 6774, M44']

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
        plt.scatter(bp_rp, abs_Gmag, s = 0.5, label = file.split('_filtered.csv')[0])

    # The y axis is reversed because smaller magnitude values mean brighter stars,and the convention is to put brighter stars at the top
    plt.ylim(16, -4)

    plt.ylabel(r'Absolute magnitude [Gaia G-band]')
    plt.xlabel('B-R color [Gaia Bp & Rp bands]')

    plt.title('Color Magnitude Diagram of Stars in the Alpha-Per, NGC 188, NGC 6774, and M44 Clusters')

    plt.legend()
    plt.show()

print(color_magnitude_diagram(csv_files))



### PLOTTING THE GIVEN ISOCHRONES IN A COLOR MAGNITUDE DIAGRAM ###

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
isochrones = [iso_filtered_1, iso_filtered_2, iso_filtered_3]

iso_names = ['logAge = 7.5', 'logAge = 8.5', 'logAge = 9.5']
def color_magnitude_diagram_iso(isochrones):
    for i in range(len(isochrones)):

        # Pull out the color & magnitude values from Gaia
        app_Gmag = isochrones[i]['Gmag']
        bp_rp = isochrones[i]['bp_rp']

        # Creating the Color Magnitude Diagram
        if (isochrones[i].any() == iso_filtered_1.any()).any():
            plt.scatter(bp_rp, app_Gmag, s = 0.7, label = iso_names[i])

    # The y axis is reversed because smaller magnitude values mean brighter stars,and the convention 
    # is to put brighter stars at the top
    plt.ylim(25, -10)

    plt.ylabel('G magnitude')
    plt.xlabel('BP-RP color')

    plt.title('Color Magnitude Diagram of Three Isochrones')

    plt.legend()
    plt.show()

print(color_magnitude_diagram_iso(isochrones))


### CREATING A FUNCTION FOR EACH CLUSTER AND ITS FIT ###
def cluster_fit(cluster, isochrone):
    cluster_csv = pd.read_csv(cluster)
    # query_result_filtered = query_result.dropna(subset=['phot_g_mean_mag'])
    # query_result_filtered = query_result.dropna(subset=['bp_rp'])

    # Pull out the color & magnitude values from the cluster and from the corresponding isochrone
    app_Gmag_cluster = cluster_csv['phot_g_mean_mag']
    bp_rp_cluster = cluster_csv['bp_rp']

    app_Gmag_iso = isochrone['Gmag']
    bp_rp_iso = isochrone['bp_rp']

    # Calculating distance from parallax 
    parallax_Signal = cluster_csv['parallax']
    parallax_in_arcsec = parallax_Signal/1000 #convert from milliarcseconds to arcseconds
    d = 1/parallax_in_arcsec

    # Calculating absolute magnitude using distance 
    abs_Gmag_cluster = app_Gmag_cluster - 5*np.log10(d/10)

    # Creating the Color Magnitude Diagram plot
    plt.scatter(bp_rp_cluster, abs_Gmag_cluster, s = 0.5, label = cluster)
    plt.scatter(bp_rp_iso, app_Gmag_iso, s = 0.7, label = 'isochrone')

    # The y axis is reversed because smaller magnitude values mean brighter stars,and the convention is to put brighter stars at the top
    plt.ylim(16, -4)

    plt.ylabel(r'Absolute magnitude [Gaia G-band]')
    plt.xlabel('B-R color [Gaia Bp & Rp bands]')

    plt.title('Color Magnitude Diagram of Stars in the Alpha-Per, NGC 188, NGC 6774, and M44 Clusters')

    plt.legend()
    plt.show()


### PLOTTING ALPHA PERSEI WITH ITS BEST FIT ISOCHRONE ###
print(cluster_fit('alpha_per_filtered.csv', iso_filtered_1))


### PLOTTING NGC 188 WITH ITS BEST FIT ISOCHRONE ###



### PLOTTING NGC 6774 WITH ITS BEST FIT ISOCHRONE ###



### PLOTTING M 44 WITH ITS BEST FIT ISOCHRONE ###


