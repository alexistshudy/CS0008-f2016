# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: October 28, 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Assignment 2 - Python Script

#define function: printKV(key,value,klen=0)
def printKV(key,value,klen=0):
    #define the "width" as the maximum of the key itself or the specified key
    width = max(len(key),klen)
    widthvalue = str(width)
    #define value formatting depending on variable type of value using isinstance
    if isinstance(value, str):
        print(format(key,widthvalue),":",format(value,'20'))
    elif isinstance(value, int):
        print(format(key,widthvalue), ":", format(value, '10,d'))
    elif isinstance(value, float):
        print(format(key,widthvalue), ":", format(value, '10,.3f'))

#define function: processFile(fh)
def processFile(fh):
    open_file = open(fh)
    #readline
    #rstrip
    # initialize counter and agregator variables at 0
    line_count = 0
    total_distance = 0
    #For loop, runs through each line, adds one to counter and adds distance column to total_distance
    for line in open_file:
        #can be combined into two lines:
            #[name, distance] = line.rstrip('\n').split(',')
            #distance = float(distance)
        #use .rstrip to remove new line created at the end
        line = line.rstrip("\n")
        #split string using .split; split on comma deliminator
        split_line = line.split(",")
        #assign second column to distance variable and convert to float
        distance = float(split_line[1])
        #add one to counter and add distance to total distance
        line_count += 1
        total_distance += distance

    #print file-specific totals using printKV formatting
    #use a constant instead of entering 25 on each of them...
    #substitute print statements for a return, then print outside of the function
    printKV("File Name",filename,25)
    printKV("Partial Total # of Lines",line_count,25)
    printKV("Partial distance run",total_distance,25)

    #add file-level totals to overall distance and linecounts, overall variables are global vars
    global overall_distance
    global overall_linecount
    overall_distance += total_distance
    overall_linecount += line_count

    #print using printKV format for Totals
    print("Totals")
    printKV("Total Number of Lines",overall_linecount,25)
    printKV("Total Distance Run", overall_distance,25)

    #close the file
    open_file.close()

# Start Main script
#ask for user input, includes instructions for stopping/quiting the program
userinput = str(input("Please enter the name of the file you would like to use. Or to quit, please enter 'quit' or 'q'"))
overall_distance = 0
overall_linecount = 0

#while loop tests user input & calls processFile function
while userinput != "quit" and userinput != "q" and userinput != "":
    filename = userinput
    processFile(filename)
    userinput = str(input("Would you like to process another file? Please enter the name of the file you would like to use. Or to quit, please enter 'quit' or 'q'"))



#to ensure that the file exists in the directory... start the script with import os.path
#in while loop, check as part of the conditions: and os.path.exists(file)

# MN: you forgot to print the overall totals

