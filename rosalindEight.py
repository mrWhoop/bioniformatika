sDNA = input("Input DNA string: ")

sRNA = ""

for i in sDNA:
    if i == "T":
        sRNA += "U"
    else:
        sRNA += i

print(sRNA)
