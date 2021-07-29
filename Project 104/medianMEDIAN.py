import csv

f = open("heightWeight.csv")
csvObject = csv.reader(f)

fileData = list(csvObject)
fileData.pop(0)
weight = []
median = 0

for i in range(len(fileData)):
    h = float(fileData[i][2])
    weight.append(h)

weight.sort()

if (len(weight)%2!=0):
    median = float(weight[len(weight)//2])
elif(len(weight)%2==0):
    m = [weight[len(weight)//2],weight[(len(weight)//2)-1]]
    add = m[0] + m[1]
    median = add/2

print("Median : " + str(median))
    

    