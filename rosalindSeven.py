s = input("Input DNA string: ")

countA = 0
countC = 0
countG = 0
countT = 0

for i in s:
    if i == "A":
        countA = countA + 1
    elif i == "C":
        countC = countC + 1
    elif i == "G":
        countG = countG + 1
    elif i == "T":
        countT = countT + 1
    else:
        print("Unknown character in string.")

print(countA, countC, countG, countT)
