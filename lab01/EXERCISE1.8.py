# Write a program that displays your name inside a box on the screen, like this:+------+ ¦ Dave ¦ +------+

name = input("WRITE YOUR NAME(NOT SURNAME): ")
space = " "

if len(name) % 2 == 0:
    if len(name) == 4:
        space *= 5
    elif len(name) == 6:
        space *= 4
    elif len(name) == 8:
        space *= 3
    elif len(name) == 10:
        space *= 2
    elif len(name) == 12:
        space *= 1
    else:
        print("ARE U KIDDING ME? IT'S NOT EVEN NAME!!")
        exit()
    print("+ - - - - - - -+")
    print(f"¦              ¦")
    print(f"¦{space}{name}{space}¦")
    print(f"¦              ¦")
    print("+ - - - - - - -+")
else:
    if len(name) == 3:
        space *= 6
    elif len(name) == 5:
        space *= 5
    elif len(name) == 7:
        space *= 4
    elif len(name) == 9:
        space *= 3
    elif len(name) == 11:
        space *= 2
    elif len(name) == 13:
        space *= 1
    else:
        print("ARE U KIDDING ME? IT'S NOT EVEN NAME!!")
        exit()
    print("+ - - - - - - - +")
    print(f"¦               ¦")
    print(f"¦{space}{name}{space}¦")
    print(f"¦               ¦")
    print("+ - - - - - - - +")
