filename = str(input("Would you like to process another file?"))
lines = []
open_file = open(filename)
for line in open_file:
    name, dist = line.strip().split(',')
    lines.append((name,dist))
print(lines)



from collections import defaultdict

#masterdata = {'Mary':2,12.5),('John':1,15.2),('Mary':2,30.7),('Tom':1,120.6)]
#masterdata = [("Mary",12.5),("John",15.2),("Mary",30.7),("Tom",120.6)]
#masterdatac = counter(masterdata)
#print(masterdatac)

#Casts d as a dictionary using the defaultdict function from collections
#d = defaultdict(list)
#defaultdict(list,{})
#for each elementi n the list, set the first value to name second to dist
#for name, dist in masterdatac:
        #uses collections module to append new names as new keys & for repeat names append additional dist values to the list for the same key
        #d[name].append(dist)
#print the dictionary as a test
#print(d)