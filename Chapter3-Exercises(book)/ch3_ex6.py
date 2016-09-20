# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: sept 19 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 3, Exercise 5: Mass and Weight

# ask for user inputs (day, month, year)
month = int(input("Enter month: "))
day = int(input("Enter day: "))
year = int(input("Enter year (two digits): "))

#Calculate & return magic message
if month*day == year:
    print("This date is magic")
else:
    print("This date is not magic")