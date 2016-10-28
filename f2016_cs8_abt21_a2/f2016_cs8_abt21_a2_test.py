# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: October 28, 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Assignment 2 - Python Script

# Ask user for file name; indicate instructions for closing the program.

#filename = str(input("Please enter the name of the file you would like to use. Or to quit, please enter 'quit' or 'q'"))
#open_file = open(filename,'r')
#ReadLine
#line = open_file.readline()
#Split String
#split_line = line.split(',')
#Define distance variable
#distance = split_line[1]
#print(distance)

filename = "f2016_cs8_a2.data.1.csv"
distance = 5000.50
count = 50
#define function: printKV(key,value,klen=0)
def printKV(key,value,klen=0):
    #define the "width" as the maximum of the key itself or the specified key
    width = max(len(key),klen)
    widthvalue = str(width)
    #define value formatting depending on variable type of value
    if isinstance(value, str):
        print(format(key,widthvalue),":",format(value,'20'))
    elif isinstance(value, int):
        print(format(key,widthvalue), ":", format(value, '10,d'))
    elif isinstance(value, float):
        print(format(key,widthvalue), ":", format(value, '10,.3f'))
#
printKV("File Name",filename, 20)
printKV("Distance", distance, 20)
printKV("Count", count, 20)






#define function: processFile(fh)
#def processFile(fh):
    #open_file = open(fh,'r')
    #readline
    #rstrip
    # count number of lines
    #line_count = 0
    #for line in open_file:
        #line_count += 1
    #print("Number of Lines:", line_count)

    #restult = total_distance
    #dist_line = 0
    #for line in open_file:
        #dist_line = int(open_file.readline())
        #dist_line = strip
    #print("Distance" dist_line)
#while userinput != "quit" and userinput != "q" and userinput != "":

#filename = userinput
#processFile(filename)




