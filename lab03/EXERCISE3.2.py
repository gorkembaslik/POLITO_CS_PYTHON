# Write a program that translates a letter grade into the corresponding numerical grade.
# The marks in letters are A, B, C, D and F, possibly followed by a + or - sign. Their
# numerical values are, in order, 4, 3, 2, 1 and 0. The grades F + and F– do not exist. A
# + sign increases the numerical grade by 0.3, while a - sign decreases it by the same
# amount. The A+ grade is however equal to 4.0.
# Enter a letter grade: B–
# The numeric value is 2.7. [P3.12]

a = input("Enter a letter grade: ")
a = a.upper()

if len(a) == 1:
    a = a + " "

if a[0] == "A":
    if a[1] == " ":
        b = 4
    elif a[1] == "+":
        b = 4
    elif a[1] == "-":
        b = 3.7
    else:
        print("CHECK WHAT YOU WROTE AFTER A")
        exit()
elif a[0] == "B":
    if a[1] == "+":
        b = 3.3
    elif a[1] == " ":
        b = 3
    elif a[1] == "-":
        b = 2.7
    else:
        print("CHECK WHAT YOU WROTE AFTER B")
        exit()
elif a[0] == "C":
    if a[1] == "+":
        b = 2.3
    elif a[1] == " ":
        b = 2
    elif a[1] == "-":
        b = 1.7
    else:
        print("CHECK WHAT YOU WROTE AFTER C")
        exit()
elif a[0] == "D":
    if a[1] == "+":
        b = 1.3
    elif a[1] == " ":
        b = 1
    elif a[1] == "-":
        b = 0.7
    else:
        print("CHECK WHAT YOU WROTE AFTER D")
        exit()
elif a[0] == "F":
    if a[1] == " ":
        b = 0
    else:
        print(f"THE GRADE {a} DO NOT EXIST.")
        exit()
else:
    print("CHECK WHAT YOU WROTE")
    exit()

print(f"The numeric value is: {b}")
