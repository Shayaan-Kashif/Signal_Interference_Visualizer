import math
import numpy as np
import matplotlib.pyplot as plt

print("\nWelcome to the Singal Inrterfercen visualizer!!!")
print("Please enter the following information about your waves to have them visualized.")

#Speed of light constant 
c = 3*math.pow(10,8)


#Collecting information about wave 1
print("\n----For Wave 1----")
amplitude  = input("What is the amplitude in volts?: ")
while(type(amplitude)== str):
    try:
       amplitude = float(amplitude)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        amplitude  = input("What is the amplitude in volts?: ")

frequency = input("What is the frequency in Hz?: ")
while(type(frequency)== str):
    try:
        frequency = float(frequency)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        frequency = input("What is the frequency in Hz?: ")

phase = input("What is the intial phase of the wave in radians?: ")
while(type(phase)== str):
    try:
       phase = float(phase)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        phase = input("What is the intial phase of the wave in radians?: ")

x1 = input("What would you like as your fixed distance?: ")
while(type(x1)== str):
    try:
         x1 = float(x1)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        x1 = input("What would you like as your fixed distance?: ")

t1 = input("What would you like as your fixed time?: ")
while(type(t1)== str):
    try:
        t1 = float(t1)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        t1 = input("What would you like as your fixed time?: ")



#Collecting information about wave 2
print("\n----For Wave 2----")
amplitude2  = input("What is the amplitude in volts?: ")
while(type(amplitude2)== str):
    try:
       amplitude2 = float(amplitude2)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        amplitude2  = input("What is the amplitude in volts?: ")

frequency2 = input("What is the frequency in Hz?: ")
while(type(frequency2)== str):
    try:
        frequency2 = float(frequency2)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        frequency2 = input("What is the frequency in Hz?: ")

phase2 = input("What is the intial phase of the wave in radians?: ")
while(type(phase2)== str):
    try:
        phase2 = float(phase2)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        phase2 = input("What is the intial phase of the wave in radians?: ")

x2 = input("What would you like as your fixed distance?: ")
while(type(x2)== str):
    try:
        x2 = float(x2)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        x2 = input("What would you like as your fixed distance?: ")

t2 = input("What would you like as your fixed time?: ")
while(type(t2)== str):
    try:
        t2 = float(t2)
    except(ValueError):
        print("\nSorry you did not enter a valid input")
        t2 = input("What would you like as your fixed time?: ")

#Computing Angular Frequencies 
angular_frequency = 2 * math.pi * int(frequency)
angular_frequency2 = 2 * math.pi * int(frequency2)

#Computing Wave Lengths 
wave_length = c/int(frequency)
wave_length2 = c/int(frequency2)

#Computing Wave Numbers 
wave_number = (2*math.pi)/int(wave_length)
wave_number2 = (2*math.pi)/int(wave_length2)


# Time domain plot
t = np.linspace(0, 1 / frequency, 1000)  
wave1_time = amplitude * np.sin(angular_frequency * t - wave_number * x1 + phase)
wave2_time = amplitude2 * np.sin(angular_frequency2 * t - wave_number2 * x2 + phase2)

summed_wave_time = wave1_time + wave2_time

plt.figure(figsize=(12, 12))#Size of the window

# Ploting Wave 1 and Wave 2 in Time Domain
plt.subplot(4, 1, 1)
plt.plot(t, wave1_time, label="Wave 1")
plt.plot(t, wave2_time, label="Wave 2")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.title("Time Domain Plot - Wave 1 and Wave 2")
plt.legend()
plt.grid(True)

# Ploting Summed Wave in Time Domain
plt.subplot(4, 1, 2)
plt.plot(t, summed_wave_time, label="Summed Wave (Time Domain)", color="purple")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.title("Time Domain Plot - Summed Wave")
plt.legend()
plt.grid(True)



#Space domain plot
x = np.linspace(0, 2 * max(wave_length, wave_length2), 1000)  # Space values
wave1_space = amplitude * np.sin(wave_number * x - angular_frequency * t1 + phase)
wave2_space = amplitude2 * np.sin(wave_number2 * x - angular_frequency2 * t2 + phase2)

summed_wave_space = wave1_space + wave2_space

# Ploting Wave 1 and Wave 2 in Space Domain
plt.subplot(4, 1, 3)
plt.plot(x, wave1_space, label="Wave 1")
plt.plot(x, wave2_space, label="Wave 2")
plt.xlabel("Position (m)")
plt.ylabel("Amplitude (V)")
plt.title("Space Domain Plot - Wave 1 and Wave 2")
plt.legend()
plt.grid(True)

# Ploting Summed Wave in Space Domain
plt.subplot(4, 1, 4)
plt.plot(x, summed_wave_space, label="Summed Wave (Space Domain)", color="purple")
plt.xlabel("Position (m)")
plt.ylabel("Amplitude (V)")
plt.title("Space Domain Plot - Summed Wave")
plt.legend()
plt.grid(True)

#Showing the plots
plt.tight_layout()
plt.show()

