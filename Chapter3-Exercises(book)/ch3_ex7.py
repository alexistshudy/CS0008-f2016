# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: sept 19 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 3, Exercise 7: Color Mixer

#red&blue = purple, red&yellow = orange, blue&yellow = green

#ask user to input 2 primary colors
color_1 = input("Enter primary color 1 to be mixed (red, yellow, or blue)")
color_2 = input("Enter primary color 2 to be mixed (red, yellow, or blue)")

#check for correct input
if color_1 == 'red' and color_2 == 'blue':
    print("purple")
elif color_1 == 'blue' and color_2 == 'red':
    print("purple")
elif color_1 == 'blue' and color_2 == 'yellow':
    print("green")
elif color_1 == 'yellow' and color_2 == 'blue':
    print("green")
elif color_1 == 'yellow' and color_2 == 'red':
    print("orange")
elif color_1 == 'red' and color_2 == 'yellow':
    print("orange")
else:
    print("error, those are not two primary colors")