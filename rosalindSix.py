s = input("Input string: ")

slovar = {}

for word in s.split(' '):
    if word in slovar:
        slovar[word] = slovar[word] + 1
    else:
        slovar[word] = 1

for key, value in slovar.items():
    print(key, value)
