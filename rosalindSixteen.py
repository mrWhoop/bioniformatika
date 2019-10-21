import math
from Bio.SeqUtils import GC

DNA = input("Input DNA string: ")
numbers = input("Input values between 0 and 1: ").split(" ")

A = [float(i) for i in numbers]

B = []

for i in A:
    logForB = 0
    for j in DNA:
        if j == "G" or j == "C":
            logForB += math.log(i/2, 10)
        else:
            logForB += math.log((1 - i) / 2, 10)
    B.append(logForB)

for i in B:
    print(i)
