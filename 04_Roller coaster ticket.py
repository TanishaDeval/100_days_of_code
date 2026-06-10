print("Welcome to Roller Coaster!")
height=float(input("What is your height?:"))
bill = 0
if height>=120:
    print("You are allowed to ride this!")
    age=int(input("What is your age?:"))
    if age>45 or age<=55:
        bill=0
        print("Free ride")
    elif age>18:
        bill = 100
        print("pay : ₹100")
    elif age<=10:
        bill =50
        print("pay : ₹50")
    elif age<=15:
        bill = 60
        print("pay : ₹60")
    else :
        bill=70
        print("pay : ₹70")
    photo = input("Do you want a photo?(y/n):")
    if photo == "y":
        bill+=3

    print(f"Your bill is ₹{bill}")

else:
    print("OOps!You should grow taller to ride on this!")