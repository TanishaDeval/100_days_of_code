print("Welcome to Python pizza delivery!")
size=input("Which size of pizza do you want?(S / M / L):")
pepperoni = input("Do you want pepperoni?(Y/N):")
extra_cheese =input("Do you want extra cheese?(Y/N):")
bill = 0

if size == "S":
    bill = 200
elif size == "M":
    bill = 400
elif size == "L":
    bill = 600
if pepperoni == "Y":
    bill +=50
if extra_cheese == "Y":
    bill+=50

print(f"Your total bill is ₹{bill}")
