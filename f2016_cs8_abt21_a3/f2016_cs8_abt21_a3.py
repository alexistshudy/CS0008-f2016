import pprint
pp = pprint.PrettyPrinter()

from collections import defaultdict
masterfile = 'f2016_cs8_a3.data.txt'

filenames = []
open_masterinput = open(masterfile)
for line in open_masterinput:
    filename = line.strip()
    filenames.append((filename))

#print(filenames)

#create master list of all records from all three files
#create empty list
records = []
#read each filename from the master input and open the file
for filename in filenames:
    open_file = open(filename)
    #skip the header row
    next(open_file)
    #read each line in the open file
    for line in open_file:
        #assign first column to name and second column to dist, use strip and split to create two distinct columns from the csv format
        name, dist = line.strip().split(',')
        dist = float(dist)
        #append name & distance to the records list
        records.append((name,dist))
    #close the file
    open_file.close()

#print records as a test
#print('Printing list "records":')
#pp.pprint(records)

#Casts d as a dictionary using the defaultdict function from collections
distance_dict= defaultdict(list)
#for each elementi n the list, set the first value to name second to dist
for name, dist in records:
    #uses collections module to append new names as new keys & for repeat names append additional dist values to the list for the same key
    distance_dict[name].append(dist)

#print the dictionary as a test
#print('Printing dictionary "distance_dict":')
#pp.pprint(distance_dict)

output_dict = defaultdict(dict)
for k,v in distance_dict.items():
    # count number of values per key (# of times each name appears in master list)
    count = (len(v))
    ind_total_dist = sum(v)
    output_dict[k] = [count,ind_total_dist]

#print('Printing dictionary "d":')
#pp.pprint(d)

#output data file with name, count, and total distance for each participant
import csv
with open('outputfile.csv', 'w') as f:
    c = csv.writer(f)
    c.writerow(['name','count','total distance'])
    for key, value in output_dict.items():
        c.writerow([key] + value)