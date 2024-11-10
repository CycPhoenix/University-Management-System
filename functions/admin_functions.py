import os

def admin_menu():
    """Menu for Administrator functions"""
    while True:
        print("\n--- Administrator Menu ---")
        print("1. Add New Course")
        print("2. Add/Remove Student")
        print("3. Manage Lecturers")
        print("4. Generate Reports")
        print("5. View All Data")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_course()
        elif choice == '2':
            add_remove_student()
        elif choice == '3':
            manage_lecturers()
        elif choice == '4':
            generate_reports()
        elif choice == '5':
            view_all_data()
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")
            
def add_course():
    """Add a new course to courses.txt file"""
    course_code = input("Enter course code: ")
    course_name = input("Enter course name: ")
    credits = input("Enter course credits: ")
    with open("data/courses.txt", "a") as f:
        f.write(f"{course_code}, {course_name}, {credits}\n")
    print("Courses added successfully.")


def add_remove_student():
    """Add or remove a student"""
    print("1. Add Student")
    print("2. Remove Student")
    choice = input("Select an option: ")

    if choice == '1':
        # Add a new student
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        department = input("Enter student department: ")
        with open("data/students.txt", "a") as f:
            f.write(f"{student_id}, {name}, {department}")
        print("Student added successfully.")
    elif choice == '2':
        # Remove an existing student
        student_id = input("Enter student ID to remove: ")
        with open("data/students.txt", "r") as f:
            lines = f.readlines()
        with open("data/students.txt", "w") as f:
            for line in lines:
                if not line.startswith(student_id):
                    f.write(line)
        print("Student removed successfully.")
    else:
        print("Invalid choice.")

def manage_lecturers():
    """Add, remove or update lecturer information"""
    print("1. Add Lecturer")
    print("2. Remove Lecturer")
    print("3. Update Lecturer Information")
    choice = input("Select an option: ")

    if choice == '1':
        # Add a new lecturer
        lecturer_id = input("Enter lecturer ID: ")
        name = input("Enter lecturer name: ")
        department = input("Enter lecturer department: ")
        with open("data/lectureres.txt", "a") as f:
            f.write(f"{lecturer_id}, {name}, {department}")
        print('Lecturer added successfully.')
    elif choice == '2':
        # Remove an existing lecturer
        lecturer_id = input("Enter lecturer ID: ")
        with open("data/lecturers.txt", 'r') as f:
            lines = f.readlines()
        with open("data/lecturers.txt", "w") as f:
            for line in lines:
                if not line.startswith(lecturer_id):
                    f.write(line)
        print("Lecturer removed successfully.")
    elif choice == '3':
        # Update lecturer information
        lecturer_id = input("Enter lecturer ID: ")
        update_name = input("Enter new name: ")
        update_department = input("Enter new department: ")
        with open("data/lecturers.txt", 'r') as f:
            lines = f.readlines()
        with open("data/lecturers.txt", 'w') as f:
            for line in lines:
                if line.startswith(lecturer_id):
                    f.write(f"{lecturer_id}, {update_name}, {update_department}\n")
                else:
                    f.write(line)
        print("Lecturer information updated successfully.")
    else:
        print("Invalid choice.")

def generate_reports():
    """Generate a report of total students, active courses, and lecturers"""
    # Count students
    if os.path.exists("data/students.txt"):
        with open("data/stuents.txt", "r") as f:
            student_count = len(f.readlines())
    else:
        student_count = 0

    # Count courses
    if os.path.exists("data/courses.txt"):
        with open("data/courses.txt", "r") as f:
            course_count = len(f.readlines())
    else:
        course_count = 0

    # Count lecturers
    if os.path.exists("data/lecturers.txt"):
        with open("data/lecturers.txt", "r") as f:
            lecturer_count = len(f.readlines())
    else:
        lecturer_count = 0

    # Diaplay the report
    print("\n--- University Report ---")
    print(f"Total Students: {student_count}")
    print(f"Total Active Courses: {course_count}")
    print(f"Total Lecturers: {lecturer_count}")

def view_all_data():
    """View all data for students, courses, and lecturers"""
    print("\n--- All Data ---")

    # Display student data
    if os.path.exists("data/students.txt"):
        with open("data/students.txt", "r") as f:
            students = f.readlines()
            for student in students:
                print(student.strip())
    else:
        print("No student data available.")

    # Display course data
    if os.path.exists("data/courses.txt"):
        with open("data/courses.txt", "r") as f:
            courses = f.readlines()
            for course in courses:
                print(course.strip())
    else:
        print("No course dataavailable.")

    # Display lecturer data
    if os.path.exists("data/lecturers.txt"):
        with open ("data/lecturers.txt", "r") as f:
            lecturers = f.readline()
            for lecturer in lecturers:
                print(lecturer.strip())
    else:
        print("No lecturer data available.")