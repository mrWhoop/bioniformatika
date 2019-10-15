import itertools

alphabet = list(input("Vnesi abecedo: ").split(" "))
num = int(input("Vnesi dolzino besede: "))

prod = [''.join(x) for x in itertools.product(alphabet, repeat=num)]

prod = sorted(prod)

for i in prod:
    print(i)
