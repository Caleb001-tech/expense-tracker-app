username = "admin"
password = "1234"
def login():
    user=input("enter username")
    pin = input("enter password")

    if user == "admin":
        print("yes")
    else:
        print("no")
    if password == "1234":
        print("correct password")
    else:
        print("incorrect password")


login()

