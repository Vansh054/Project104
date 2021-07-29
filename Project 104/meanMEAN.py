import csv

f = open("heightWeight.csv")
csvObject = csv.reader(f)

fileData = list(csvObject)
fileData.pop(0)
weight = []
add = 0
mean = 0

for i in range(len(fileData)):
    h = float(fileData[i][2])
    weight.append(h)
    add = add + h
    
mean = add/len(weight)
print("Mean : " + str(mean))
