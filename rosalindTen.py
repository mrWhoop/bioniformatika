import numpy as np

dataSet = open("files/rosalind_gc.txt", "r")
data = dataSet.read().splitlines()
dataSet.close()

seq = ""

for i in data:
    seq += i

workSet = seq.split(">")
workSet.remove('')

highLabel = ""
high = 0

for i in workSet:
    label = i[0:13:1]
    DNA = i[13::]
    countAll = 0
    countCG = 0

    for j in DNA:
        if j == "C" or j == "G":
            countCG = countCG + 1
            countAll = countAll + 1
        else:
            countAll = countAll + 1

    perc = countCG/countAll

    if perc > high:
        high = perc
        highLabel = label

print(highLabel)
print(high * 100)
