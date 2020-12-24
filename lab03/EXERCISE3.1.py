# Write a program that reads three numbers and displays the message “increasing” if
# they are in ascending order, “decreasing” if they are in descending order and
# “neither” if they are neither in ascending nor descending order. In this Exercise
# increasing strictly means increasing, i.e. each value must be greater than the previous
# one (the same meaning has the term decreasing): the sequence 3 4 4, therefore,
# should not be considered increasing. [P3.5]

a = []

for n in range(1, 4):
    a.append(int(input(f"WRITE {n}. NUMBER: ")))

if a[0] > a[1] > a[2]:
    print("SYSTEM MESSAGE: DECREASING")
elif a[0] < a[1] < a[2]:
    print("SYSTEM MESSAGE: INCREASING")
else:
    print("SYSTEM MESSAGE: NEITHER INCREASING NOR DECREASING")

print(a)
print(" ------>")
