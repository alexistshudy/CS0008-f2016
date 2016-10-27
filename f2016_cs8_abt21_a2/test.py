filename = input("Enter File name: ")
open_file = open(filename,'r')
line = open_file.readline()
print(line)
