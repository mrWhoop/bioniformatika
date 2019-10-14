DNA = input("Input DNA string: ")
subDNA = input("Input DNA substring: ")

counter = len(subDNA)
i = 0

while i < len(DNA) - counter:
    if DNA[i:i+counter] == subDNA:
        print(i+1)
    i += 1
