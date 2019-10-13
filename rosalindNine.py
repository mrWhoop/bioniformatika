sDNA = input("Input DNA string: ")
complementDNA = ""

for i in sDNA:
    if i == "A":
        complementDNA += "T"
    elif i == "T":
        complementDNA += "A"
    elif i == "C":
        complementDNA += "G"
    elif i == "G":
        complementDNA += "C"
    else:
        print("Sth wrong.")

print(complementDNA[::-1])
