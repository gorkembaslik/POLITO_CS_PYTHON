# Imagine that you and a number N of friends go to a luxury restaurant, and when you
# ask for the bill, you want to split the total amount and the tip (15 percent) between
# all. Write a pseudocode for calculating the amount of money that everyone has to
# pay. Your program should print the amount of the bill, the tip, the total cost, and the
# amount each person has to pay. It should also print how much of what each person
# pays is for the bill and for the tip

bill= float(input("BILL: "))
friends = int(input("HOW MANY FRIENDS: "))

tip = bill * 15/100
totalAmount = bill + tip
eachPersonPays = totalAmount / (friends+1)
eachPersonTip = tip / (friends+1)
eachPersonBill = bill/ (friends+1)

print(f"The bill is {bill}$, the tip you have to pay {tip:.2f}$, the total amount {totalAmount:.2f}$,"
      f" the amount each person have to pay {eachPersonPays:.2f}$")
