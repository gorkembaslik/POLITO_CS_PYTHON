import random

degerler = list()

sayac = [0, 0, 0, 0, 0, 0]

for i in range(10000):
    degerler.append(random.randint(1, 6))

for a in degerler:
    if a == 1:
        sayac[0] += 1
    elif a == 2:
        sayac[1] += 1
    elif a == 3:
        sayac[2] += 1
    elif a == 4:
        sayac[3] += 1
    elif a == 5:
        sayac[4] += 1
    elif a == 6:
        sayac[5] += 1


print(sayac)
