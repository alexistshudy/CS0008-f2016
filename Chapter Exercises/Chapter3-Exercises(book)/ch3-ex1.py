# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: sept 19 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 3, Exercise 1: Day of the Week

# ask user for number 1-7
inputday = float(input("Enter a number 1-7: "))

#conditions & error message
if inputday == 1:
    print("Monday")
elif inputday == 2:
    print("Tuesday")
elif inputday == 3:
    print("Wednesday")
elif inputday == 4:
    print("Thursday")
elif inputday == 5:
    print("Friday")
elif inputday == 6:
    print("Saturday")
elif inputday == 7:
    print("Sunday")
else:
    print("Error! You did not enter a nubmer between 1 and 7")
