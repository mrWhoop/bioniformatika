f = open("files/fiveTest", "r")
f2 = open("files/fiveTestRez", "w")

c = 0

while True:
    line = f.readline()
    if not line:
        break

    if c % 2 == 1:
        f2.write(line)
    c = c + 1

f.close()
f2.close()
