import math

DNA = input("Input DNA string: ")
numbers = input("Input values between 0 and 1: ").split(" ")

A = [float(i) for i in numbers]

countAll = 0
countCG = 0

for j in DNA:
    if j == "C" or j == "G":
        countCG = countCG + 1
        countAll = countAll + 1
    else:
        countAll = countAll + 1

GC = countCG/countAll

B = []

for i in A:
    B.append(math.log(GC) - math.log(i)) #klele

print(B)
