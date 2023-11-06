print("\n\nPython pizza")
print("-------------")
print("Menu")
print("----\n")
print("Large Pizza: $6.00")
print("Extra Large pizza: $10.00")
print("Toppings: 1 = $1.00, 2 = $1.75, 3 = $2.50, 4 = $3.35\n\n")
print("Order Instructions")
print("------------------")
print("For extra large pizza, please type XL \nFor large pizza, please type L\n")
size = input("Which size pizza would you like?\n")

pizza_price = [6.0,10.0]
toppings_price = [1.0, 1.75, 2.5, 3.35]
sub_total = 0.00

if str(size) == 'L' or str(size) == 'XL':
    toppings = input("How many toppings would you like? Type a number between 1-4\n")
    if int(toppings) > 4:
        print("Please choose 1-4 toppings only")
    elif int(toppings) < 1:
        print("Please choose 1-4 toppings only")
    else:
        print("You have chosen", size, "pizza and", toppings, "toppings!")
        if str(size) == 'L':
            sub_total = pizza_price[0]
        elif str(size) == 'XL':
            sub_total = pizza_price[1]

        if int(toppings) == 1:
            sub_total = sub_total + toppings_price[0]
        elif int(toppings) == 2:
            sub_total = sub_total + toppings_price[1]
        elif int(toppings) == 3:
            sub_total = sub_total + toppings_price[2]
        elif int(toppings) == 4:
            sub_total = sub_total + toppings_price[3]
else:
    print("Please choose either a L or XL pizza only.\n")

taxes = float(sub_total) * 0.13
total_price = float(sub_total) + taxes
print("\nYour order summary:")
print("Sub total: $",format(sub_total, ".2f"), "Taxes: $",format(taxes, ".2f"), "Amount due: $",format(total_price, ".2f"))