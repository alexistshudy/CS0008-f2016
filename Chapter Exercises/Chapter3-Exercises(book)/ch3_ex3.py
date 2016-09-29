# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: sept 19 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 3, Exercise 3: Age Classifier

#ask user for age
age = float(input("Enter your age: "))

#if statements
if age <= 1:
    print("Infant")
elif age >= 1 and age < 13:
    print ("Child")
elif age >= 13 and age < 20:
    print ("Teenager")
else:
    print("Adult")
