#implementing read write operations etc
#case study 1

var_name = open("file1.txt", "r")
for each in var_name:
    print(each)

file_read = open("file1.txt", "r")
print(file_read.read())

#splitting
with open("file1.txt","r") as data:
    data_1 = data.readlines()
    for line in data_1:
        var = line.split()
        print(var)
