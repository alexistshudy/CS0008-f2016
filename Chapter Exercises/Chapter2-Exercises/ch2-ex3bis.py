# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: 03/09/2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Online exercise set, Exercise 3

# 1 acre = 4,046.85664224 sq meters

# Asks for sq meter input
sqm = float(input('Enter total square meters of land: '))

# Calculates acres
var_acres = sqm/4046.85664224

#Prints acres
print("Acres = {:.2f}".format(var_acres))