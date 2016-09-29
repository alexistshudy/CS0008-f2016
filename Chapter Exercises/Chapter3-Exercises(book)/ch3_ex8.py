# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: sept 19 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Starting with Python, Chapter 3, Exercise 7: Hot Dog Cookout Calculator

#ask user for input
number_of_guests = int(input("How many guests are attending? "))
hotdogs_per_guest = int(input("How many hotdogs will each guest be given? "))

#calculate # of hotdogs needed
hotdogs_needed = number_of_guests * hotdogs_per_guest

#determine packages of hotdogs and buns
package_hotdogs = hotdogs_needed / 10
package_buns = hotdogs_needed / 8
leftover_hotdogs = int(package_hotdogs)*10 - hotdogs_needed
leftover_buns = int(package_buns)*8 - hotdogs_needed


if leftover_buns > leftover_hotdogs
