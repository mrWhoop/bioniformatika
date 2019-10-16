import numpy as np

dataSet = open("files/rosFifteen", "r")
data = dataSet.read().splitlines()
dataSet.close()

data = data[1:]
dataString = ""
for i in data:
    dataString = dataString + i

print(dataString)

P = np.zeros(len(data), dtype=int)
P[0] = -1

#position = 1
#candidate = 0
#
#while position < len(data):
#    if data[position] == data[candidate]:
#        P[position] = P[candidate]
#    else:
#        P[position] = candidate
#        candidate = P[candidate]
#        while candidate >= 0 and data[position] != data[candidate]:
#            candidate = P[candidate]
#    position += 1
#    candidate += 1
#P[position] = candidate

i = 0
j = -1
b = np.zeros(len(dataString)+1, dtype=int)

b[i] = j
while i < len(dataString):
    while j >= 0 and dataString[i] != dataString[j]:
        j = b[j]
    i += 1
    j += 1
    b[i] = j

dataSet = open("files/rosFifteenRez", "w")

for i in b:
    dataSet.write(str(i) + " ")
