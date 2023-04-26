"""
DESCRIPTION:
For this assignment, we had to make code to plot the Planck Function and the 
Rayleigh-Jeans Law. 

The Planck Function describes the brightness of the radiation emitted by a 
blackbody that is in thermal equilibrium at a specified temperature T.

The Rayleigh-Jeans Law is an approximation of the Planck Function in the long
wavelength limit. 

For this assignment, I used some code from the following Stack Overflow page:
https://stackoverflow.com/questions/22417484/plancks-formula-for-blackbody-spectrum

"""

# Imports
import matplotlib.pyplot as plt
import numpy as np

# Below are the variables for the constants in the Planck Function
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

# Defining the Planck Function 
def planck(wav_1, T_1):
    a = 2.0*h*c**2
    b = h*c/(wav_1*k*T_1)
    intensity_planck = a/ ( (wav_1**5) * (np.exp(b) - 1.0) )
    return intensity_planck

# Defining the Rayleigh-Jeans Law
def rayleigh_jeans(wav_2, T_2):
    x = 2.0*c*k*T_2
    y = wav_2**4
    intensity_rj = x/y
    return intensity_rj


# Generate x-axis in increments from 1nm to 3 micrometer in 1 nm increments
# Starting at 1 nm to avoid wav = 0, which would result in division by zero.
wavelengths = np.arange(1e-9, 3e-6, 1e-9)


# Intensities at 5770 Kelvin
intensity_planck5770 = planck(wavelengths, 5770.)
intensity_rj5770 = rayleigh_jeans(wavelengths, 5770.)


# Plotting the two functions:

# Planck-Function = red line
plt.plot(wavelengths*1e9, intensity_planck5770, 'r-', label = 'Planck Function')

# Rayleigh-Jeans Law = green line
plt.plot(wavelengths*1e9, intensity_rj5770, 'g-', label = 'Rayleigh-Jeans Law')

plt.ylim(0.0, 3.0e13)
plt.xlabel('Wavelength (in nanometers)')
plt.ylabel('Intensity')
plt.title('Blackbody Spectrum for T = 5770 Kelvin')
plt.legend()
plt.figure(figsize = (11, 9))

plt.show()