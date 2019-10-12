s = input("enter string: ")
a, b, c, d = [int(x) for x in input("Enter the 4 values: ").split()]

b = b+1
d = d+1

firstSub = s[a:b]
secondSub = s[c:d]

print(firstSub, secondSub)