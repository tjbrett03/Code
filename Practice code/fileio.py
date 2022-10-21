# Thomas Brett CYB 267
filename = "namesandcredits.csv"
myfile = []
with open(filename, 'r') as fileread:
    for line in fileread:
        myfile.append(line.split(","))
GPA = [3.8, 4.0, 4.2, 2.0]
m = 0
for k in myfile:
    print(k)

