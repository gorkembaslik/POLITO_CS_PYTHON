# Write a program that initializes a string variable and prints the first three characters, followed by three
# periods, and then the last three characters.
# For example, if the string is initialized to "Mississippi", then print Mis...ppi.

a = input("WRITE SOMETHING: ")
dot = "."
if len(a) == 7:
    dot = dot
elif len(a) == 8:
    dot *= 2
elif len(a) >= 9:
    dot *= 3
else:
    print(a)
    exit()

print(f"{a[0:3]}{dot}{a[-3:]}")
