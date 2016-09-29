# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: 03/09/2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 2, Exercise 4: Total Purchase


# Ask for the price for each item
price1 = float(input('Enter price for item 1 '))
price2 = float(input('Enter price for item 2 '))
price3 = float(input('Enter price for item 3 '))
price4 = float(input('Enter price for item 4 '))
price5 = float(input('Enter price for item 5 '))

# Calculate the subtotal as sum of all prices
subtotal = float(price1+price2+price3+price4+price5)

# Calculate the sales tax at 6% of subtotal
sales_tax = subtotal*0.06

# Calculate the total
total = subtotal+sales_tax

# Print subtotal, sales tax, and total
print('Subtotal:',subtotal,"Sales Tax (6%):",sales_tax,"Total:",total)