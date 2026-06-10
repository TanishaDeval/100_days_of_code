print("Welcome to BMI Calculator")
height=float(input("Enter your height in metres :"))
weight=float(input("Enter your weight in kg :"))
bmi=(weight/(height**2))

print(round(bmi))