print("welcome to my password strength checker")

password = input("Enter your password: ")
new = password.lower()
if len(new) >= 8:
    print("your password length is verified")
else:
    print("your password is too short")
if "@" in new:
    print("")
else:
    print("your password must contain a symbol, like @ ")
print("The first half of your password is", password[0:len(password)//2])
print("The last 3 characters of your password is", password[-3:])
