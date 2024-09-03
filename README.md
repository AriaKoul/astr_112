# ASTR 112 - Physics of Stars 

This repository contains all the code for the assignments I did for ASTR 112, Physics of Stars, which is an upper division class at UCSC.

The work in this repository includes analyzing the Gaia Catalog, which is a catalog that contains characteristics, such as distance, luminosities, and location, of more than a billion stars in the night sky. I downloaded star data from the [Gaia Esa Archive](https://gea.esac.esa.int/archive/) and converted it into csv files, which I then filtered based on given baselines. The data is in the "Data Files" folder. Using the filtered data, I developed python programs to create color magnitude diagrams and HR Diagrams that represent various stars' properties. 

## How to Use 

## File Descriptions
`using_gaia_dr2.py`: This script creates a Hertzsprung Russell Diagram and a Color Magnitude Diagram of stars that fit certain parameters (which are stated in the file). Necessary files to run this code: 
* `gaia_dr2_result.csv`

`plotting_planck_function.py`: This script plots the Planck Function which describes the brightness of the radiation emitted by a blackbody that is in thermal equilibrium at a specified temperature T. The script also plots the Rayleigh-Jeans Law which describes the Planck Function in the long wavelength limit. 

`analyzing_M67.py`: This script creates a Color Magnitude Diagram of stars in the M67 Star Cluster. Necessary files to run this code: 
* `M67_data.csv`

`main_sequence_turnoff.py`:

`analyzing_praesepe.py`: 


## Dependencies

