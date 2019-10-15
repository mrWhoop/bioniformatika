dataSet = open("files/rosFifteen", "r")
data = dataSet.read().splitlines()
dataSet.close()

data = data[1:]

print(data)
