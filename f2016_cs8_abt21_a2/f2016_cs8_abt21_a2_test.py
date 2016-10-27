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


#define function: printKV(key,value,klen=0)
def printKV(key,value,klen):
    #define the "width" as the maximum of the key itself or the specified key
    width = max(len(key),klen)
    print width
    #define value formatting depending on value type
    type(value)
    print type

printKV(Distance,15,3)






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




