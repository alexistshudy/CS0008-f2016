# Asks for user input
purchase_amount = float(input('Enter purchase amount '))

# Calculates state tax, county tax, total tax, and total

state_tax = .04*purchase_amount
county_tax = .02*purchase_amount
total_tax = float(state_tax+county_tax)
total = purchase_amount+total_tax

# Prints Info
print("Purchase Amount:",purchase_amount,"State Tax:",state_tax,"County Tax:",county_tax,"Total Sales Tax:",total_tax,"Total:",total)
