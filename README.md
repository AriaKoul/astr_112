# ASTR 112 - Physics of Stars 

This repository contains all the code for the assignments I did for ASTR 112, Physics of Stars, which is an upper division class at UCSC.

The work in this repository includes analyzing the Gaia Catalog, which is a catalog that contains characteristics, such as distance, luminosities, and location, of more than a billion stars in the night sky. I downloaded star data from the [Gaia Esa Archive](https://gea.esac.esa.int/archive/) and converted it into csv files, which I then filtered based on given baselines. The data is in the "Data Files" folder. Using the filtered data, I developed python programs to create color magnitude diagrams (CMDs) and Hertzsprung Russel (HR) Diagrams that represent various stars' properties. 

## Dependencies

## File Descriptions
`using_gaia_dr2.py`: This script creates a HR Diagram and a CMD of stars that fit certain parameters (which are stated in the file). Necessary files to run this code: 
* `gaia_dr2_result.csv`

`plotting_planck_function.py`: This script plots the Planck Function which describes the brightness of the radiation emitted by a blackbody that is in thermal equilibrium at a specified temperature T. The script also plots the Rayleigh-Jeans Law which describes the Planck Function in the long wavelength limit. 

`analyzing_M67.py`: This script creates a CMD of stars in the M67 star clusters. Necessary files to run this code: 
* `M67_data.csv`

`analyzing_praesepe.py`: This script creates a CMD of stars in the M44 star cluster which is also known as the Praesepe Cluster. Necessary files to run this code:
* `praesepe_data.csv`

`main_sequence_turnoff.py`: In this script, I analyzed four different star clusters: Alpha Persei, NGC 188, NGC 6774, and M44. I created CMDs for each star cluster, then compared them with CMDs of three given isochrones, which are curves on the HR diagram that represent a group of stars all of the same age but different masses. Using the comparison, I was able to find the approximate age of the four star clusters I was working with. Necessary files to run this code: 
* `alpha_per_filtered.csv`
* `NGC188_filtered.csv`
* `NGC6774_filtered.csv`
* `M44_filtered.csv`
* `iso.csv`
* `iso_with_bp_rp.csv`


## How to Use
Clone this repository using the following code:

`$ git clone https://github.com/AriaKoul/astr_112`

Run `python _filename_`. In place of _filename_, write any of the five python files you want to run. 

