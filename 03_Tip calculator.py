print("Welcome to the tip calculator!")

total_bill=float(input("What was the total bill?:₹"))
tip=int(input("What percentage tip would you like to give?:" ))
tip_rupees=(tip/100)*total_bill
print(f"Your tip will be of : ₹{tip_rupees}")
final_bill=total_bill+tip_rupees
print(f"Your final bill is ₹{final_bill}")
people=int(input("How many people to split the bill?:"))
bill_per_person=final_bill/people
print(f"Each person should pay : ₹{bill_per_person}")















