# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: sept 27 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Assignment 1 - Python Program

# Ask users for inputs
user_system = input("What measurement system would you like to use? (Enter 'Metric' or 'USC' and press enter) ")
if user_system == 'Metric':
    user_distance = float(input("Enter distance driven in kilometers "))
    user_gas = float(input("Enter amount of gas used in liters "))
elif user_system == 'USC':
    user_distance = float(input("Enter distance driven in miles "))
    user_gas = float(input("Enter amount of gas used in gallons "))
else:
    print('You did not enter an accepted measurement system')

#Converts user inputs to metric and USC depending on the system the user chose
if user_system == 'Metric':
    miles = user_distance * 1.60934
    km = user_distance
    gallons = user_gas * 3.78541
    liters = user_gas
elif user_system == 'USC':
    miles = user_distance
    km = user_distance / 1.60934
    gallons = user_gas
    liters = user_gas / 3.78541

#Calculate consumption
mpg = miles/gallons
cm = 100 * liters/km

#Assign Rating
if cm > 20:
    rating = 'Extremely Poor'
elif cm > 15:
    rating = 'Poor'
elif cm > 10:
    rating = 'Average'
elif cm > 8:
    rating = 'Good'
elif cm <= 8:
    rating = 'Excellent'

#Printing
print('             ','\tUSC','\tMetric')
print('Distance____:',format(miles,'9,.3f'),format(km,'9,.3f'))
print('Gas_________:',format(gallons,'9,.3f'),format(liters,'9,.3f'))
print('Consumption_:',format(mpg,'9,.3f'),format(cm,'9,.3f'))
print('Rating:',rating)


