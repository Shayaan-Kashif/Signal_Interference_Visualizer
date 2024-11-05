import math

print("\nWelcome to the Singal Inrterfercen visualizer!!!")
print("Please enter the following information about your waves to have them visualized.")

#Speed of light constant 
c = 3*math.pow(10,8)


#Collecting information about wave 1
print("\n----For Wave 1----")
amplitude  = input("What is the amplitude in volts?: ")
frequency = input("What is the frequency in Hz?: ")
phase = input("What is the intial phase of the wave in radians?: ")
x1 = input("What would you like as your fixed distance?: ")
t1 = input("What would you like as your fixed time?: ")


#Collecting information about wave 2
print("\n----For Wave 2----")
amplitude2  = input("What is the amplitude in volts?: ")
frequency2 = input("What is the frequency in Hz?: ")
phase2 = input("What is the intial phase of the wave in radians?: ")
x2 = input("What would you like as your fixed distance?: ")
t2 = input("What would you like as your fixed time?: ")


#Computing Angular Frequencies 
angular_frequency = 2 * math.pi * frequency
angular_frequency2 = 2 * math.pi * frequency2

#Computing Wave Lengths 
wave_length = c/frequency
wave_length2 = c/frequency2

#Computing Wave Numbers 
wave_number = (2*math.pi)/wave_length
wave_number2 = (2*math.pi)/wave_length2

