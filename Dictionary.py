students = {

}
while True:
    print("add or update students  ---1")
    print("remove students   ---2")
    print("view all students   ---3")
    print("exit   ---4")
    choice = input("Enter your choice: ")
    if choice == "1":
        name1 = input("Enter student name: ")
        score1 = input("Enter student score: ")
        if name1 in students:
            print("Student {} already exists".format(name1))
        else:
            students.update({name1: score1})
            print("student added successfully")
            print("student score added successfully")
    if choice == "2":
        name2 = input("Enter student name: ")
        score2 = input("Enter student score: ")
        if name2 not in students:
            print("Student {} does not exist".format(name2))
        else:
            students.pop(name2)
            print("student removed successfully")
            print("student score removed successfully")
    if choice == "3":
        print(students)
    if choice == "4":
        print("exiting.........")
        break
