print("students course enrolment tracker")
students = []
courses = set()

def add_Student():
    name = input("Enter student name: ")
    course_number = int(input("Enter number of courses: "))
    students_course = []
    students_scores = {}
    for i in range(course_number):
        course = input(f"Enter course {i+1} name: ")
        score = float(input(f"Enter score for {course}: "))
        students_course.append(course)
        students_scores[course] = score
        courses.add(course)

    student = {
        "name": name,
        "courses": students_course,
        "scores": students_scores,
    }
    students.append(student)
    print("Students added successfully")
def display_students():
    for student in students:
        print(student["name"])
        print(student["courses"])
        print(student["scores"])
def calculate_average(student):
    score = student["scores"].values()
    if len(score) == 0:
        return 0
    total = sum(score)
    average = total / len(score)
    return average
def top_students():
    best = students[0]
    best_average = calculate_average(best)
    for student in students:
        average = calculate_average(student)
        if average > best_average:
            best = student
    print("Best student is ", best["name"])
    print("Best average is ", best_average)

def showcourses():
    if len(courses) == 0:
        print("No courses available")
        return
    for course in courses:
        print(course)
    print("total courses: ", len(courses))
    print()

def remove_student():
    name = input("Enter student name: ")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            print("Student removed successfully")
            return
    print("Student not found")

def search_student():
    name = input("Enter student name: ")
    for student in students:
        if student["name"] == name:
            print(student["name"])
            print(student["courses"])
            print(student["scores"])
            return
    print("Student not found")

def menu():
    while True:
        print("1. Add student")
        print("2. Display students")
        print("3. top students")
        print("4. Show courses")
        print("5. Remove student")
        print("6. Search student")
        print("7. calculate average")
        print("8. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_Student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            top_students()
        elif choice == "4":
            showcourses()
        elif choice == "5":
            remove_student()
        elif choice == "6":
            search_student()
        elif choice == "7":
            calculate_average(input("Enter student name: "))
        elif choice == "8":
            print("Thank you for using this program")
            break
        else:
            print("Invalid choice")
menu()










            #next project
print("welcome to my expense tracker🖲️🖲️🖲️")
expenses = []
def add_expense():
    category = input("Please enter the category of your  expense:  ")
    cap= category.capitalize()
    amount = float(input(f"Enter amount of {cap}:  "))
    expenses.append({"category" : cap, "amount💲" : amount})
    print("expenses added successfully1")
def show_summary():
    print("the summary of all expenses is", expenses)
def remove_expense():
    caps = input("Please enter the category of your  expense:  ")
    if caps not in expenses:
        print("The expense you entered doesn't exist")
    else:
        expenses.remove(caps)
def main():
    while True:
        print("add expense  ---1")
        print("remove expenses  ---2")
        print("show expense summary ---3")
        print("exit   ---4")
        choice = int(input("Please enter your choice:  "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            remove_expense()
        elif choice == 3:
            show_summary()
        elif choice == 4:
            print("Thank you for using my expense tracker. exiting........")
            break
