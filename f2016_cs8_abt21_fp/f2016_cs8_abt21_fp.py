#import collections module for casting to dictionary
from collections import defaultdict

#import csv for csv output
import csv

#define class Participant
class Participant:
    #initialize an instance
    def __init__(self,name,distance,runs):
        self.name = name
        self.distance = distance
        self.runs = runs

    #define method: add_distance
    #add a single distance to the distance accumulator and increments runs by 1. Argument d is a single float
    def add_distance(d):
        distance = d

    #define method: add_distances
    #add an array of distances to the distance accumulator. Argument ld is a list of floats
    def add_distances(ld):
        self.distance = sum(ld)

    #define method: get_name
    #Returns the name of the participant of the current instance
    def get_name(self):
        return (self.name)

    #define method: get_distance
    #Returns the current value of the distance accumulator
    def get_distance(self):
        return self.distance

    #define method: get_runs
    #Returns the current value of the runs accumulator
    def get_runs(self):
        return self.runs

    #define method: __str___
    #Returns a string with name, total distance, and runs as per formatting specified in assignment
    def __str__(self):
        return '{:>20}'.format(self.name.rstrip()) + ',' + '{:4d}'.format(self.runs) + ',' + '{:9.4f}'.format(self.distance)

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

# initialize overall accumulator variables, to be updated with each new file input
overall_filecount = 0
overall_distance = 0
overall_line_count = 0

#ask user for master file name
#assumes masterfile and all datafiles are in the same directory or a path is specified

masterinput = input("Please enter the name of your master file")

#create a list of file names from masterfile
#initialize empty list, filenames
filenames = []
#open master file
open_masterinput = open(masterinput)
#each line in the masterinputis a filename, append each filename to the list, filenames
for line in open_masterinput:
    filename = line.strip()
    filenames.append(filename)
#close master file
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
    #skip header row
    next(open_file)
    #read each line in the open file
    for line in open_file:
        #use strip and split to separate csv columns in the files
        name, dist = line.strip().split(',')
        #cast distances as type float
        dist = float(dist)
        #add one to line_counter and add dist to total_distance
        line_count += 1
        total_distance += dist
        #append naem & addistance to the records list
        records.append(name,dist)
    #add to overall accumulator varialbles
    overall_filecount += 1
    overall_line_count += line_count
    overall_distance += total_distance
    #close the file
    open_file.close()
# print processing summary using printKV function
#print processing summary using printKV function (# of input files read, number of lines read, total distance run)
printKV('Number of input files read',overall_filecount,FORMAT_KEY_LENGTH)
printKV('Total number of lines read',overall_line_count,FORMAT_KEY_LENGTH)
printKV('Total distance run',overall_distance,FORMAT_KEY_LENGTH)

#Uses collections module, defaultdict to create a dictionary - combines repeat records with expected output as name: [dist1, dist2...]
#initialize distance_dict using default dict form collections
distance_dict= defaultdict(list)
#for each element in the records list, set the first value to name second to dist
for name, dist in records:
    #uses collections module to append new names as new keys & for repeat names append additional dist values to the list for the same key
    distance_dict[name].append(dist)

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


#initialize accumulator to count nubmer of participants with multiple records
repeat_count = 0

#initialize empty list, all_p to store each new class instance
#uses class Participant from distance_dict
all_p = []
#loop through each key, value pair in distance dict (key = name; value = [dist1, dist2,...]
for name, dist in distance_dict.items():
    if len(dist) == 1:
        #p is a new instance of participant class with runs = 1; and distance = to the one and only value in the distance list
        p = Participant(name,dist[0],1)
    elif len(dist) > 1:
        # p is a new instance of participant class with runs = len(dist), and initial distance 0
        p = Participant(name,0,len(dist))
        #use add_distances to set participant distances to the sum of the distance list
        p.add_distances(dist)
        #add one to repeat count accumulator to indicate that they are a participant with multiple records
        repeat_count += 1
    #append instance of Participant "p" to all_p list
    all_p.append(p)

#output all_p to a csv
#output data file with name, count, and total distance for each unique participant
#assumes outputfile is in same directory or path is specified
with open('f2016_cs8_abt21_fp.data.output.csv', w) as f:
    c = csv.writer(f, delimiter=',',escapechar=' ',quoting = csv.QUOTE_NONE)
    #create header row
    c.writerow(['name','count','total_distance'])
    #write each class isntance as a row on the csv
    for p in all_p:
        c.writerow([p.get_name().rstrip(),p.get_runs],'{:.2f}'.format(p.get_distance())])

#closefile
f.close()

#calculate participant count as length of all_p list
participant_count = len(all_p)

#print participant counts & repeat counts
printKV('Total number of participants',participant_count,FORMAT_KEY_LENGTH)
printKV('# participants w/ multiple records',repeat_count, FORMAT_KEY_LENGTH)
