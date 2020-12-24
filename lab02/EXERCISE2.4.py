numberOfBooks = int(input("NUMBER OF BOOKS: "))
totalBookPrice = float(input("TOTAL BOOK PRICE: "))

tax = totalBookPrice * 7.5 / 100
shipping = numberOfBooks * 2
orderTotal = totalBookPrice + tax + shipping

print(f"Total Book Price: {totalBookPrice}\nTax:               {tax}\nShipping:          {float(shipping)}\n+______________________ \n"
      f"Total:            {orderTotal}")
