print("Mateusz's pizza")
print("Menu")
print("Large Pizza: six dollars")
print("Extra large pizza: ten dollars")
print("Toppings: 1 = $1.00, 2 = $1.75, 3 = $2.50, 4 = $3.35")
size = input("Which size pizza would you like?")
toppings = input("How many toppings would you like?")

if toppings > 4:
    print("Please choose 1-4 toppings only please")
elif toppings <= 0:
    print("Please choose 1-4 toppings only please")
else:
    print("")