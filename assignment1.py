name = input("Enter your name: ")
clean = name.strip()
clean = clean.lower()
print("your name is", clean)
print("The first three letters of your name is", clean[0:3])
print("The last three letters of your name is", clean[-3:])
if "john" in clean:
    print("Your name contains John")
else:
    print("Your name does not contain John")



































