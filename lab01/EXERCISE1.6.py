# Write a program that prints the balance of an account after the first, second, and third year.
# The account has an initial balance of $1,000 and earns 5 percent interest per year.

balance = 1000
interest = 5/100

for n in range(1, 4):
    balance += balance * interest
    if n == 1:
        order = "st"
    elif n == 2:
        order = "nd"
    else:
        order = "rd"
    print(f"The balance of an account after the {n}{order} year is ${int(balance)} ")
