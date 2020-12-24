yazi = input("write smt")
sesli = "aeiouAEIOU"
sesliSayac = 0

for i in yazi:
    if i in sesli:
        sesliSayac += 1

print(f"Sesli harf sayısı = {sesliSayac}")
