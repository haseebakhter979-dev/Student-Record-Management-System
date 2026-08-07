import csv
import os

FILE_NAME = "students.csv"

# -----------------------------
# Create File
# -----------------------------
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Class", "Department", "CGPA", "Phone"])


# -----------------------------
# Read Data
# -----------------------------
def read_data():
    students = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


# -----------------------------
# Write Data
# -----------------------------
def write_data(students):

    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = ["ID", "Name", "Age", "Class", "Department", "CGPA", "Phone"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(students)


# -----------------------------
# Add Student
# -----------------------------
def add_student():

    students = read_data()

    student_id = input("Enter Student ID : ")

    for s in students:
        if s["ID"] == student_id:
            print("Student ID Already Exists!")
            return

    name = input("Enter Name : ")
    age = input("Enter Age : ")
    student_class = input("Enter Class : ")
    department = input("Enter Department : ")
    cgpa = input("Enter CGPA : ")
    phone = input("Enter Phone : ")

    students.append({
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Class": student_class,
        "Department": department,
        "CGPA": cgpa,
        "Phone": phone
    })

    write_data(students)

    print("\nStudent Added Successfully!\n")


# -----------------------------
# View Students
# -----------------------------
def view_students():

    students = read_data()

    if len(students) == 0:
        print("\nNo Record Found\n")
        return

    print("\n" + "="*90)
    print(f"{'ID':<8}{'NAME':<20}{'AGE':<6}{'CLASS':<10}{'DEPT':<12}{'CGPA':<8}{'PHONE'}")
    print("="*90)

    for s in students:

        print(f"{s['ID']:<8}{s['Name']:<20}{s['Age']:<6}{s['Class']:<10}{s['Department']:<12}{s['CGPA']:<8}{s['Phone']}")

    print("="*90)# -----------------------------
# Search Student
# -----------------------------
def search_student():

    students = read_data()

    search = input("Enter Student ID : ")

    for s in students:

        if s["ID"] == search:

            print("\nStudent Found\n")

            print("ID :", s["ID"])
            print("Name :", s["Name"])
            print("Age :", s["Age"])
            print("Class :", s["Class"])
            print("Department :", s["Department"])
            print("CGPA :", s["CGPA"])
            print("Phone :", s["Phone"])

            return

    print("\nStudent Not Found\n")


# -----------------------------
# Update Student
# -----------------------------
def update_student():

    students = read_data()

    student_id = input("Enter Student ID : ")

    for s in students:

        if s["ID"] == student_id:

            print("\nLeave Blank To Keep Old Value\n")

            name = input(f"Name ({s['Name']}): ")
            age = input(f"Age ({s['Age']}): ")
            student_class = input(f"Class ({s['Class']}): ")
            department = input(f"Department ({s['Department']}): ")
            cgpa = input(f"CGPA ({s['CGPA']}): ")
            phone = input(f"Phone ({s['Phone']}): ")

            if name != "":
                s["Name"] = name

            if age != "":
                s["Age"] = age

            if student_class != "":
                s["Class"] = student_class

            if department != "":
                s["Department"] = department

            if cgpa != "":
                s["CGPA"] = cgpa

            if phone != "":
                s["Phone"] = phone

            write_data(students)

            print("\nStudent Updated Successfully\n")

            return

    print("\nStudent Not Found\n")


# -----------------------------
# Delete Student
# -----------------------------
def delete_student():

    students = read_data()

    student_id = input("Enter Student ID : ")

    new_students = []

    found = False

    for s in students:

        if s["ID"] != student_id:

            new_students.append(s)

        else:

            found = True

    if found:

        write_data(new_students)

        print("\nStudent Deleted Successfully\n")

    else:

        print("\nStudent Not Found\n")


# -----------------------------
# Total Students
# -----------------------------
def total_students():

    students = read_data()

    print("\nTotal Students :", len(students), "\n")


# -----------------------------
# Sort By Name
# -----------------------------
def sort_students():

    students = read_data()

    students.sort(key=lambda x: x["Name"].lower())

    print("\nStudents Sorted By Name\n")

    print("=" * 90)

    print(f"{'ID':<8}{'NAME':<20}{'AGE':<6}{'CLASS':<10}{'DEPT':<12}{'CGPA':<8}{'PHONE'}")

    print("=" * 90)

    for s in students:

        print(f"{s['ID']:<8}{s['Name']:<20}{s['Age']:<6}{s['Class']:<10}{s['Department']:<12}{s['CGPA']:<8}{s['Phone']}")

    print("=" * 90)# -----------------------------
# Main Menu
# -----------------------------
def menu():

    while True:

        print("\n")
        print("=" * 50)
        print("     STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Total Students")
        print("7. Sort Students")
        print("8. Exit")

        choice = input("\nEnter Your Choice : ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            total_students()

        elif choice == "7":
            sort_students()

        elif choice == "8":

            print("\nThank You For Using Student Record Management System")
            break

        else:

            print("\nInvalid Choice! Please Try Again.")


# -----------------------------
# Program Starts Here
# -----------------------------
create_file()
menu()