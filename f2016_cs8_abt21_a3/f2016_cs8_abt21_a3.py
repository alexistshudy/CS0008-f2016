# name: Alexis Tshudy
# email: abt21@pitt.edu
# date: November 21, 2016
# class: CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
# description: Assignment 3 - Python Script

from collections import defaultdict

# length of the key, constant, for use in printKV function
FORMAT_KEY_LENGTH = 35

#define printKV function (from instructor solution a2)
def printKV(key,value,klen = 0):
    # check which is the length to be used when printing the key
    # max of klen and the length of key
    klen = max(klen,len(key));
    # check which is type of value and choose the proper formatting
    if isinstance(value,str):
        # we have a string
        fvalue = '20s'
    elif isinstance(value,float):
        # we have a float
        fvalue = '10.3f'
    elif isinstance(value,int):
        # we have a integer
        fvalue = '10d'
    else:
        # we do not know what we have,
        # so we try our best to convert it to a string and
        # format it as a string
        value = str(value)
        fvalue = '20s'
    # end if
    #
    # print key and value with correct formatting
    print(format(key,str(klen)+'s'),' : ',format(value,'<'+fvalue))
# end def

#initialize overall accumulator variables, to be updated with each new file input
overall_filecount = 0
overall_distance = 0
overall_line_count = 0

#initialize participant count accumulator variables
repeat_count = 0
participant_count = 0

#select masterfile
masterfile = 'f2016_cs8_a3.data.txt'

#create a list of file names from masterfile
#initialize empty list
filenames = []
#open masterfile
open_masterinput = open(masterfile)
#each line in the masterfile is a filename, append each filename to the empty list, "filenames"
for line in open_masterinput:
    filename = line.strip()
    filenames.append((filename))
#close masterfile
open_masterinput.close()

#create master list of all name, distance records from all three files
#initialize empty list
records = []
#read each filename from the master input and open that file
for filename in filenames:
    #initialize partial accumulator variables
    line_count = 0
    total_distance = 0
    #open the file
    open_file = open(filename)
    #skip the header row
    next(open_file)
    #read each line in the open file
    for line in open_file:
        #assign first column to name and second column to dist, use strip and split to create two distinct columns from the csv format
        name, dist = line.strip().split(',')
        #cast distnaces as type float
        dist = float(dist)
        #add one to line_counter and add dist to total_distance
        line_count += 1
        total_distance += dist
        #append name & distance to the records list
        records.append((name,dist))
    #add to overall accumulator variables
    overall_filecount += 1
    overall_line_count += line_count
    overall_distance += total_distance
    #close the file
    open_file.close()

#Uses collections module, defaultdict to create a dictionary - combines repeat records with expected output as name: [dist1, dist2...]
#initialize distance_dict using default dict form collections
distance_dict= defaultdict(list)
#for each element in the records list, set the first value to name second to dist
for name, dist in records:
    #uses collections module to append new names as new keys & for repeat names append additional dist values to the list for the same key
    distance_dict[name].append(dist)

#Uses collections module, defaultdict to create a dictionary - with expected output name: [# of distance entries, total distance]
#initialize output_dict using default dict form collections
output_dict = defaultdict(dict)
#given name and distances from the dictionary
for name,dist in distance_dict.items():
    #count the number of items/keys (these are unique participants)
    participant_count += 1
    #count number of values per name (# of distnace values = # times each name appears in master list)
    count = (len(dist))
    #add one to repeat_count if a participant has more than one value
    if count >1:
        repeat_count += 1
    #sum distances for each name, cast as a variable
    ind_total_dist = sum(dist)
    #create output in new dictionary as name : [# of distance entries, total distance]
    output_dict[name] = [count,ind_total_dist]

#print processing summary using printKV function (# of input files read, number of lines read, total distance run)
printKV('Number of input files read',overall_filecount,FORMAT_KEY_LENGTH)
printKV('Total number of lines read',overall_line_count,FORMAT_KEY_LENGTH)
printKV('Total distance run',overall_distance,FORMAT_KEY_LENGTH)

#find max and min distance values, cast as two separate vales (participant & value)
#(adapted from https://dbader.org/blog/python-min-max-and-nested-lists)

#max
max_dist = max(records, key=lambda x: x[1])
max_part,max_dist = max_dist
#min
min_dist = min(records, key=lambda x: x[1])
min_part,min_dist = min_dist

#print min & max values per assignment formatting using printKV function
#max
printKV('Max distance run',max_dist,FORMAT_KEY_LENGTH)
printKV('   by participant',max_part,FORMAT_KEY_LENGTH)
#min
printKV('Min distance run',min_dist,FORMAT_KEY_LENGTH)
printKV('   by participant',min_part,FORMAT_KEY_LENGTH)

#print participant counts & repeat counts
printKV('Total number of participants',participant_count,FORMAT_KEY_LENGTH)
printKV('# participants w/ multiple records',repeat_count, FORMAT_KEY_LENGTH)

#output data file with name, count, and total distance for each participant
import csv
with open('outputfile.csv', 'w') as f:
    c = csv.writer(f)
    #create header row
    c.writerow(['name','count','total distance'])
    for key, value in output_dict.items():
        c.writerow([key] + value)