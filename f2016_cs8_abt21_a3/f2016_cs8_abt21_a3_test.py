from collections import defaultdict

# length of the key
FORMAT_KEY_LENGTH = 35

#printKV function
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


masterfile = 'f2016_cs8_a3.data.txt'
#create a list of file names from masterfile
#initialize empty list
filenames = []
#open masterfile
open_masterinput = open(masterfile)
#each line in the masterfile is a file name, append each filename to the empty list, filenames
for line in open_masterinput:
    filename = line.strip()
    filenames.append((filename))

#print(filenames)

#create master list of all records from all three files
#create empty list
records = []
#read each filename from the master input and open the file
for filename in filenames:
    #initialize partial accumulator variables
    line_count = 0
    total_distance = 0
    open_file = open(filename)
    #skip the header row
    next(open_file)
    #read each line in the open file
    for line in open_file:
        #assign first column to name and second column to dist, use strip and split to create two distinct columns from the csv format
        name, dist = line.strip().split(',')
        dist = float(dist)
        ##add one to counter and add dist to total distance
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

#Casts d as a dictionary using the defaultdict function from collections
distance_dict= defaultdict(list)
#for each elementi n the list, set the first value to name second to dist
for name, dist in records:
    #uses collections module to append new names as new keys & for repeat names append additional dist values to the list for the same key
    distance_dict[name].append(dist)

#min_dist = min(records, key=lambda x: x[1])
#print(min_dist)

output_dict = defaultdict(dict)

for k,v in distance_dict.items():
    participant_count += 1
    # count number of values per key (# of times each name appears in master list)
    count = (len(v))
    if count >1:
        repeat_count += 1
    # sum distances
    ind_total_dist = sum(v)
    #create output as 'k' :
    output_dict[k] = [count,ind_total_dist]

#print processing summary (# of input files read, number of lines read, total distance run)
printKV('Number of input files read',overall_filecount,FORMAT_KEY_LENGTH)
printKV('Total number of lines read',overall_line_count,FORMAT_KEY_LENGTH)
printKV('Total distance run',overall_distance,FORMAT_KEY_LENGTH)

#find max and min distance values (notation from https://dbader.org/blog/python-min-max-and-nested-lists)
max_dist = max(records, key=lambda x: x[1])
max_part,max_dist = max_dist
min_dist = min(records, key=lambda x: x[1])
min_part,min_dist = min_dist

printKV('Max distance run',max_dist,FORMAT_KEY_LENGTH)
printKV('   by participant',max_part,FORMAT_KEY_LENGTH)

printKV('Min distance run',min_dist,FORMAT_KEY_LENGTH)
printKV('   by participant',min_part,FORMAT_KEY_LENGTH)

#print participant counts & repeat counts
printKV('Total number of participants',participant_count,FORMAT_KEY_LENGTH)
printKV('# participants w/ multiple records',repeat_count, FORMAT_KEY_LENGTH)


#output data file with name, count, and total distance for each participant
import csv
with open('outputfile.csv', 'w') as f:
    c = csv.writer(f)
    c.writerow(['name','count','total distance'])
    for key, value in output_dict.items():
        c.writerow([key] + value)