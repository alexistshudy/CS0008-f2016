# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: October 28, 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Assignment 2 - Python Script

# Ask user for file name; indicate instructions for closing the program.

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


userinput = str(input("Please enter the name of the file you would like to use. Or to quit, please enter 'quit' or 'q'"))
overall_distance = 0
overall_linecount = 0

#define function: processFile(fh)
def processFile(fh):
    open_file = open(fh)
    #readline
    #rstrip
    # initialize counter and agregator variables at 0
    line_count = 0
    total_distance = 0
    #need to fix...
    for line in open_file:
        #use rstrip to remove new line
        line = line.rstrip("\n")
        #split string using .split
        split_line = line.split(",")
        #assign second column to distance variable and convert to float
        distance = float(split_line[1])
        #add one to counter and at distance to total distance
        line_count += 1
        total_distance += distance
    printKV("File Name",filename,20)
    printKV("Partial Total # of Lines",line_count,20)
    printKV("Partial distance run",total_distance,20)

    global overall_distance
    global overall_linecount
    overall_distance += total_distance
    overall_linecount += line_count
    print("Totals")
    printKV("Total Number of Lines",overall_linecount,20)
    printKV("Total Distance Run", overall_distance,20)

while userinput != "quit" and userinput != "q" and userinput != "":
    filename = userinput
    processFile(filename)
    userinput = str(input("Please enter the name of the file you would like to use. Or to quit, please enter 'quit' or 'q'"))




