# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: sept 19 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 3, Exercise 2: Area of a rectangle

# Ask for rectangles' length & width
length_1 = float(input("Enter length of rectangle 1: "))
width_1 = float(input("Enter width of rectangle 1: "))
length_2 = float(input("Enter length of rectangle 2: "))
width_2 = float(input ("Enter width of rectangle 2: "))

#calcualate rectangle areas
area_1 = length_1*width_1
area_2 = length_2*width_2

#compare areas & print
if area_1 > area_2:
    print("The area of rectangle 1 is greater than the area of rectangle 2")
elif area_1 < area_2:
    print("The area of rectangle 2 is greater than the area of rectangle 1")
elif area_1 == area_2:
    print("The areas of the rectangles are the same")