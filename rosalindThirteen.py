from collections import Counter

dataSet = open("files/rosThirteen", "r")
data = dataSet.read().splitlines()
dataSet.close()

data = data[1:]

seq = ""
for i in data:
    seq += i

mer = []

i = 0
while i < len(seq)-3:
    mer.append(seq[i:i+4])
    i += 1

mer = sorted(mer)

orderedDictionary = Counter(mer)

rez = list(orderedDictionary.values())

for i in rez:
    print(i)
