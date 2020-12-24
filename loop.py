rate = 0.025
year = 0
balance = float(input("BALANCE: "))
target = 2 * balance
print(f"When the year is {2020+year}, balance is {balance:.2f}")
while balance < target:
    year = year + 1
    interest = balance * rate
    balance = balance + interest
    print(f"When the year is {2020+year}, balance is {balance:.2f}")
