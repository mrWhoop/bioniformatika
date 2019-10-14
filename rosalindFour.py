a, b = [int(x) for x in input("Enter the 2 values: ").split()]

if a % 2 != 1:
    a = a + 1

s = 0

while a <= b:
    s = s + a
    a = a + 2

print(s)