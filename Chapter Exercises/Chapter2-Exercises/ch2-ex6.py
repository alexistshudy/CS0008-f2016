# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: 03/09/2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 2, Exercise 6: Sales Tax

# Asks for user input
purchase_amount = float(input('Enter purchase amount '))

# Calculates state tax, county tax, total tax, and total
state_tax = .04*purchase_amount
county_tax = .02*purchase_amount
total_tax = float(state_tax+county_tax)
total = purchase_amount+total_tax

# Prints Info
print("Purchase Amount:",purchase_amount,"State Tax:",state_tax,"County Tax:",county_tax,"Total Sales Tax:",total_tax,"Total:",total)
