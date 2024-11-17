import os
import sys


def get_resource_path(relative_path):
    """Get the absolute path to a resource file, whether running as .py or .exe"""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    return os.path.join(base_path, relative_path)


# File paths
COURSES_FILE = get_resource_path('data/courses.txt')
STUDENTS_FILE = get_resource_path('data/students.txt')
LECTURERS_FILE = get_resource_path('data/lecturers.txt')
LECTURER_COURSES_FILE = get_resource_path('data/lecturer_courses.txt')

DATA_PATH = "data"


def admin_menu():
    """
    Menu for Administrator functions.
    Provides access to various management options for students, lecturers, and courses, as well as options to generate reports and view all data.
    """
    while True:
        print("\n--- Administrator Menu ---")
        print("1. Manage Courses")
        print("2. Add/Remove Student")
        print("3. Manage Lecturers")
        print("4. Generate Reports")
        print("5. View All Data")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            manage_courses()
        elif choice == '2':
            manage_students()
        elif choice == '3':
            manage_lecturers()
        elif choice == '4':
            generate_reports()
        elif choice == '5':
            view_all_data()
        elif choice == '6':
            print("Returning to main menu...")
            break
        else:
            print("Invalid option. Please try again.")


def manage_courses():
    """Function to manage courses (Add, Remove, and Update)."""
    while True:
        print("\n--- Manage Courses ---")
        print("1. Add a new course")
        print("2. Remove an existing course")
        print("3. Update Course Information")
        print("4. Back to Admin Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_course()
        elif choice == "2":
            remove_course()
        elif choice == "3":
            update_course_information()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def add_course():
    """Add a new course to the courses file."""
    print("\n--- Add New Course ---")
    course_code = input("Enter course code: ").strip()
    course_name = input("Enter course name: ").strip()
    credits = input("Enter course credits: ").strip()

    # Append the new course to the file
    with open(COURSES_FILE, 'a') as f:
        f.write(f"{course_code}, {course_name}, {credits}\n")
    print(f"Course '{course_name}' added successfully!")


def remove_course():
    """Remove a course from the courses file."""
    print("\n--- Remove Course ---")

    # Load all courses from the file
    with open(COURSES_FILE, 'r') as f:
        courses = f.readlines()

    if not courses:
        print("No courses available to remove.")
        return

    # Display available courses
    print("\nAvailable courses:")
    for idx, course in enumerate(courses, start=1):
        print(f"{idx}. {course.strip()}")

    # Select a course to remove
    try:
        course_index = int(input("Enter the number of the course to remove: ")) - 1
        if 0 <= course_index < len(courses):
            removed_course = courses.pop(course_index)

            # Save updated courses back to the file
            with open(COURSES_FILE, 'w') as f:
                f.writelines(courses)

            print(f"Course '{removed_course.strip()}' removed successfully!")

        else:
            print("Invalid course number. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def update_course_information():
    """Update the details of an existing course."""
    print("\n--- Update Course Information ---")

    # Load all courses from the file
    try:
        with open(COURSES_FILE, 'r') as f:
            courses = f.readlines()

    except FileNotFoundError:
        print("Courses file not found!")
        return

    if not courses:
        print("No courses available to update.")
        return

    # Display available courses
    print("\nAvailable courses:")
    for idx, course in enumerate(courses, start=1):
        print(f"{idx}. {course.strip()}")

    # Select a course to update
    try:
        course_index = int(input("Enter the number of the course to update: ")) - 1
        if 0 <= course_index < len(courses):
            selected_course = courses[course_index].strip()
            course_data = selected_course.split(',')

            # Check if the course data is complete
            if len(course_data) < 3:
                print("Incomplete course data. Please check the file format.")

            # Get updated details
            print(f"Current details: Code: {course_data[0]}, Name: {course_data[1]}, Credits: {course_data[2]}")
            new_code = input("Enter new course code (leave blank to keep current): ") or course_data[0]
            new_name = input("Enter new course name (leave blank to keep current): ") or course_data[1]
            new_credits = input("Enter new course credits (leave blank to keep current): ") or course_data[2]

            # Update the course in the list
            courses[course_index] = f"{new_code}, {new_name}, {new_credits}\n"

            # Save updated courses back to the file
            with open(COURSES_FILE, 'w') as f:
                f.writelines(courses)

            print(f"Course '{new_name}' updated successfully!")

        else:
            print("Invalid course number. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")

def manage_students():
    """
    Add, remove, or update student information.
    """
    while True:
        print("\n--- Manage Students ---")
        print("1. Add a new student")
        print("2. Remove an existing student")
        print("3. Update Student Information")
        print("4. Back to Admin Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            update_student_information()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    students_file = os.path.join(DATA_PATH, "students.txt")

    if choice == "1":
        # Add a new student
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip()
        department = input("Enter student department: ").strip()

        # Add new student to studnets.txt
        with open(students_file, "a") as f:
            f.write(f"{student_id}, {name}, {department}")
        print("Student added successfully.")

    elif choice == "2":
        # Remove an existing student
        student_id = input("Enter student ID to remove: ").strip()

        # Remove student from studnets.txt
        with open(students_file, "r") as f:
            lines = f.readlines()
        with open(students_file, "w") as f:
            for line in lines:
                if not line.startswith(student_id):
                    f.write(line)

        print("Student removed successfully.")

    elif choice == "3":
        # Update student information
        student_id = input("Enter Student ID to update: ").strip()
        new_name = input("Enter new Name: ").strip()
        new_department = input("Enter new Department: ").strip()

        # Update studnet details in students.txt
        with open(students_file, "r") as f:
            lines = f.readlines()
        with open(students_file, "w") as f:
            for line in lines:
                if line.startswith(student_id):
                    f.write(f"{student_id}, {new_name}, {new_department}")
                else:
                    f.write(line)
        print("Student information updated successfully.")

    else:
        print("Invalid choice.")


def add_student():
    """Add a new student to the students file."""
    print("\n--- Add New Student ---")
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    department = input("Enter department: ").strip()

    # Append the new student to the file
    with open(STUDENTS_FILE, 'a') as f:
        f.write(f"{student_id}, {name}, {department}\n")
    print(f"Student '{name}' added successfully!")

def remove_student():
    """Remove a student from the students file."""
    print("\n--- Remove Student ---")

    # Load all students from the file
    with open(STUDENTS_FILE, 'r') as f:
        students = f.readlines()

    if not students:
        print("No students available to remove.")
        return
    
    # Display available students
    print("\nAvailable students:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. {student.strip()}")

    # Select a student to remove
    try:
        student_index = int(input("Enter the number of the student to remove: ")) - 1
        if 0 <= student_index < len(students):
            removed_student = students.pop(student_index)

            # Save updated students back to the file
            with open(STUDENTS_FILE, 'w') as f:
                f.writelines(students)

            print(f"Student '{removed_student.strip()}' removed successfully!")

        else:
            print("Invalid student number. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")

def update_student_information():
    """Update the details of an existing student."""
    print("\n--- Update Student Information ---")

    # Load all students from the file
    try:
        with open(STUDENTS_FILE, 'r') as f:
            students = f.readlines()

    except FileNotFoundError:
        print("Students file not found!")
        return
    
    if not students:
        print("No students available to update.")
        return
    
    # Display available students
    print("\nAvailable students:")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. {student.strip()}")

    # Select a student to update
    try:
        student_index = int(input("Enter the number of the student to update: ")) - 1
        if 0 <= student_index < len(students):
            selected_student = students[student_index].strip()
            student_data = selected_student.split(",")

            # Check if the student data is complete
            if len(student_data) < 3:
                print("Incomplete student data. Please check the file format.")

            # Get updated details
            print(f"Current details: ID: {student_data[0]}, Name: {student_data[1]}, Department: {student_data[2]}")
            new_id = input("Enter new student ID (leave blank to keep current): ") or student_data[0]
            new_name = input("Enter new student name (leave blank to keep current): ") or student_data[1]
            new_department = input("Enter new department (leave blank to keep current): ") or student_data[2]

            # Update the student in the list
            students[student_index] = f"{new_id}, {new_name}, {new_department}\n"

            # Save updated students back to the file
            with open(STUDENTS_FILE, 'w') as f:
                f.writelines(students)

            print(f"Student '{new_name}' updated successfully!")

        else:
            print("Invalid student number. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")


def manage_lecturers():
    """Add, remove or update lecturer information"""
    while True:
        print("\n--- Manage Lecturers ---")
        print("1. Add Lecturer")
        print("2. Remove Lecturer")
        print("3. Update Lecturer Information")
        print("4. Assign Course to Lecturer")
        print("5. Back to Admin Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_lecturer()
        elif choice == '2':
            remove_lecturer()
        elif choice == '3':
            update_lecturer_information()
        elif choice == "4":
            assign_course_to_lecturer()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def add_lecturer():
    """Add a new lecturer to the lecturers file."""
    print("\n--- Add New Lecturer ---")
    lecturer_id = input("Enter lecturer ID: ").strip()
    name = input("Enter lecturer name: ").strip()
    department = input("Enter lecturer department: ").strip()

    # Append the new lecturer to the file
    with open(LECTURERS_FILE, 'a') as f:
        f.write(f"{lecturer_id}, {name}, {department}\n")
    print(f"Lecturer '{name}' added successfully!")

def remove_lecturer():
    """Remove a lecturer from the lecturers file."""

    # load all courses from the file
    with open(LECTURERS_FILE, 'r') as f:
        lecturers = f.readlines()

    if not lecturers:
        print("No lecturers available to remove.")

    # Display available courses
    print("Avaiable courses:")
    for idx, lecturer in enumerate(lecturers, start=1):
        print(f"{idx}. {lecturer.strip()}")

    # Select a course to remove
    try:
        lecturer_index = int(input("Enter the number of the lecturer to remove: ")) - 1
        if 0 <= lecturer_index < len(lecturers):
            removed_lecturer = lecturers.pop(lecturer_index)

            # Save updated courses back to the file
            with open(LECTURERS_FILE, 'w') as f:
                f.writelines(lecturers)

            print(f"Lecturer '{removed_lecturer.strip()}' removed successfully!")

        else:
            print("Invalid lecturer number. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")

def update_lecturer_information():
    """Update the deatils of an existing lecturer."""
    print("--- Update Lecturer Information ---")

    # Load all courses from the file
    try:
        with open(LECTURERS_FILE, 'r') as f:
            lecturers = f.readlines()

    except FileNotFoundError:
        print("Lecturers file not found!")

    if not lecturers:
        print("No lecturers available to update.")
    
    # Display available lecturers
    print("\nAvailable lecturers:")
    for idx, lecturer in enumerate(lecturers, start=1):
        print(f"{idx}. {lecturer.strip()}")

    # Select a lecturer to update
    try:
        lecturer_index = int(input("Enter the number of the lecturer to update: ")) - 1
        if 0 <= lecturer_index < len(lecturers):
            selected_lecturer = lecturers[lecturer_index].strip()
            lecturer_data = selected_lecturer.split(',')

            # Check if the lecturer data is complete
            if len(lecturer_data) < 3:
                print("Incomplete lecturer data. Please check the file format.")

            # Get updated details
            print(f"Current details: ID: {lecturer_data[0]}, Name: {lecturer_data[1]}, Department: {lecturer_data[2]}")
            new_id = input("Enter new lecturer id (leave blank to keep current): ") or lecturer_data[0]
            new_name = input("Enter new lecturer name (leave blank to keep current): ") or lecturer_data[1]
            new_department = input("Enter new department (leave blank to keep current): ") or lecturer_data[2]

            # Update the lecturer in the list
            lecturers[lecturer_index] = f"{new_id}, {new_name}, {new_department}\n"

            # Dave updated lecturers back to the file
            with open(LECTURERS_FILE, 'w') as f:
                f.writelines(lecturers)

            print(f"Lecturer '{new_name}' updated successfully!")

        else:
            print("Invalid lecturer number. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")

def assign_course_to_lecturer():
    """Assign a course to a lecturer."""
    print("\n--- Assign Course to Lecturer ---")
    lecturer_id = input("Enter lecturer ID: ").strip()
    course_code = input("Enter course code: ").strip()

    # Append the assignment to the file (assuming the file for this existsor using courses.txt as example)
    with open(LECTURER_COURSES_FILE, 'a') as f:
        f.write(f"{lecturer_id}, {course_code}\n")
    print("Course assigned to lecturer successfully!")

def generate_reports():
    """Generate various reports (e.g., list of students, lecturers, courses)."""
    while True:
        print("\n--- Generate Reports ---")
        print("1. List of Students")
        print("2. List of Lecturers")
        print("3. List of Courses")
        print("4. Back to Admin Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            print_students_report()
        elif choice == "2":
            print_courses_report()
        elif choice == "3":
            print_lecturers_report()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def print_students_report():
    """Prints a formatted list of all students."""
    print("\n--- Student Report ---")
    try:
        with open(STUDENTS_FILE, 'r') as f:
            students = f.readlines()
            if not students:
                print("No students found.")
            else:
                for student in students:
                    student_id, name, department = student.strip().split(',')
                    print(f"ID: {student_id}, Name: {name}, Department: {department}")

    except FileNotFoundError:
        print("Students file not found.")
    
def print_courses_report():
    """Prints a formatted list of all courses."""
    print("\n--- Course Report ---")
    try:
        with open(COURSES_FILE, 'r') as f:
            courses = f.readlines()
            if not courses:
                print("No courses found.")
            else:
                for course in courses:
                    course_code, course_name, credits = course.strip().split(',')
                    print(f"Code: {course_name}, Name: {course_name}, Credits: {credits}")

    except FileNotFoundError:
        print("Courses file not found.")

def print_lecturers_report():
    """Prints a formatted list of all lecturers"""
    print("\n--- Lecturer Report ---")
    try:
        with open(LECTURERS_FILE, 'r') as f:
            lecturers = f.readlines()
            if not lecturers:
                print("No lecturers found.")
            else:
                for lecturer in lecturers:
                    lecturer_id, name, department = lecturer.strip().split(',')
                    print(f"ID: {lecturer_id}, Name: {name}, Department: {department}")

    except FileNotFoundError:
        print("Lecturers file not found.")


def view_all_data():
    """View all data for students, lecturers, courses, and lecturer course assignments."""
    print("\n--- View All Data ---")

    # Display students data
    print("\n--- Students ---")
    try:
        with open(STUDENTS_FILE, 'r') as f:
            students = f.readlines()
            if students:
                for student in students:
                    print(student.strip())
            else:
                print("No students found.")

    except FileNotFoundError:
        print("Students file not found!")

    # Display lecturers data
    print("\n--- Lecturers ---")
    try:
        with open(LECTURERS_FILE, 'r') as f:
            lecturers = f.readlines()
            if lecturers:
                for lecturer in lecturers:
                    print(lecturer.strip())
            else:
                print("No lecturers found.")

    except FileNotFoundError:
        print("Lecturers file not found!")

    # Display courses data
    print("\n--- Courses ---")
    try:
        with open(COURSES_FILE, 'r') as f:
            courses = f.readlines()
            if courses:
                for course in courses:
                    print(course.strip())
            else:
                print("No courses found.")

    except FileNotFoundError:
        print("Courses file not found!")

    # Display courses data
    print("\n--- Lecturer Course Assigns ---")
    try:
        with open(LECTURER_COURSES_FILE, 'r') as f:
            lecturer_courses = f.readlines()
            if lecturer_courses:
                for lecturer_course in lecturer_courses:
                    print(lecturer_course.strip())
            else:
                print("No lecturer course found.")
    
    except FileNotFoundError:
        print("Lecturer courses file not found!")
