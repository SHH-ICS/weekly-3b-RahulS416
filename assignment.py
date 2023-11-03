print("Mateusz's pizza")
print("Menu")
print("Large Pizza: six dollars")
print("For large pizza, please type lpizza")
print("Extra large pizza: ten dollars")
print("For extra large pizza, please type xlpizza")
print("Toppings: 1 = $1.00, 2 = $1.75, 3 = $2.50, 4 = $3.35")
size = input("Which size pizza would you like?")
toppings = input("How many toppings would you like?")
lpizza = 6.00
xlpizza = 10.00
price = 0.00

if sdtxt.isnumeric(size):
    size = int(size)
if size == lpizza:
    print("You have chosen", size)
elif size == xlpizza:
    print("You have chosen", xlpizza)
else:
    print("Please choose either lpizza or xlpizza")

if txt.isnumeric(toppings):
    toppings = int(toppings)
if toppings > 4:
    print("Please choose 1-4 toppings only please")
elif toppings <= 0:
    print("Please choose 1-4 toppings only please")
else:
    print("You have chosen", toppings, "toppings")