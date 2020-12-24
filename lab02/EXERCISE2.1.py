# Write a program that prompts the user for two integers and then prints

liste = []
for n in range(1, 3):
    a = int(input(f"{n}. INTEGER: "))
    liste.append(a)

difference = liste[0] - liste[1]
product = liste[0] * liste[1]
average = (liste[0] + liste[1]) / 2
print(f"The sum: {sum(liste)} \nThe difference: {difference} \nThe product: {product} \nThe average: {average}"
      f" \nThe distance: {abs(difference)} \nThe maximum: {max(liste)} \nThe minimum: {min(liste)} ")
