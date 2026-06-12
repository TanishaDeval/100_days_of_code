import random
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z',
             'A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ["!",'@','#','$','%','&','+','-','(',')','^','*']
digits = ['1','2','3','4','5','6','7','8','9','0']
num_symbols = int(input("How many symbols do you want in your password?:"))
num_digits = int(input("How many digits do you want in your password?:"))
num_alphabets=int(input("How many alphabets do you want in your password?:"))

password_list=[]

for i in range(0,num_symbols):
    password_list += random.choice(symbols)

for i in range(0,num_digits):
    password_list += random.choice(digits)

for i in range(0,num_alphabets):
    password_list += random.choice(alphabets)
random.shuffle(password_list)

password=""
for char in password_list:
    password += char

print(f"Your password : {password}")
length = len(password)
print(f"Your password length : {length}")











