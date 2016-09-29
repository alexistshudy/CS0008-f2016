# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: sept 19 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 3, Exercise 5: Mass and Weight

# weight = mass X 9.8

#Ask user for mass
mass = float(input("Enter object mass: "))

#Calculate weight
weight = mass*9.8

#Return messages "too heavy" if weight > 500 newtons and "too light" if weight < 100 newtons
if weight > 500:
    print("Weight (in Newtons) = ",weight,"The object is too heavy")
elif weight < 100:
    print("Weight (in Newtons) = ",weight,"The object is too light")
else:
    print("Weight (in Newtons) = ",weight)