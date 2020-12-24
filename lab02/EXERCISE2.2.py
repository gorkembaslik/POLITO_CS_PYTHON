a = int(input("WRITE A 5-DIGIT INTEGER: "))
if len(str(a)) == 5:
    for n in range(len(str(a))):
        print(str(a)[n], end=" ")
else:
    print("pls write 5-DIGIT 5555555555555555")
    exit()

