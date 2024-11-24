import os
import sys


def get_resource_path(relative_path):
    """Get the absolute path to a resource file, whether running as .py or .exe"""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.join(os.path.dirname(__file__))))
    return os.path.join(base_path, relative_path)


# File paths
STUDENTS_FILE = get_resource_path('data/students.txt')
ENROLLMENTS_FILE = get_resource_path('data/enrollments.txt')
GRADES_FILE = get_resource_path('data/grades.txt')


def registrar_menu():
    """Menu for Registrar functions"""
    while True:
        print("\n--- Registrar Menu ---")
        print("1. Register New Student")
        print("2. Update Student Records")
        print("3. Manage Enrollments")
        print("4. Issue Transcripts")
        print("5. View Student Information")
        print("6. Back to Registrar Menu")
        registrar_choice = input("Select an option: ")

        if registrar_choice == '1':
            register_new_student()
        elif registrar_choice == '2':
            update_student_records()
        elif registrar_choice == '3':
            manage_enrollments()
        elif registrar_choice == '4':
            issue_transcript()
        elif registrar_choice == '5':
            view_student_information()
        elif registrar_choice == '6':
            break
        else:
            print("Invalid option. Please try again.")


def register_new_student():
    """Register a new student by adding them to students.txt"""
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    department = input("Enter student department: ").strip()

    with open(STUDENTS_FILE, 'a') as f:
        f.write(f"{student_id}, {name}, {department}")
    print("Student registered successfully")


def update_student_records():
    """Update existing student records"""
    student_id = input("Enter student ID: ").strip()
    new_name = input("Enter new name: ").strip()
    new_department = input("Enter new department: ").strip()

    # Read all data and find the student to update
    with open(STUDENTS_FILE, 'r') as f:
        lines = f.readlines()

    # Write back with updated information
    with open(STUDENTS_FILE, 'w') as f:
        for line in lines:
            if line.startswith(student_id):
                # Write updated record
                f.write(f"{student_id}, {new_name}, {new_department}")
            else:
                # Write original file
                f.write(line)
        print("Student record updated.")


def manage_enrollments():
    """Enroll a student in a specific course by adding an entry to enrollments.txt"""
    student_id = input("Enter student ID: ")
    course_code = input("Enter course code: ")

    with open(ENROLLMENTS_FILE, 'a') as f:
        f.write(f"{student_id}, {course_code}")
    print("Student enrolled in course.")


def issue_transcript():
    """Issue a transcript for a studnet by reading their grades from grades.txt"""
    student_id = input("Enter student ID for transcript: ")
    print(f"\n--- Transcript for Student ID {student_id}")

    if GRADES_FILE:
        with open(GRADES_FILE, 'r') as f:
            found = False
            for line in f:
                grade_data = line.strip().split(",")
                if grade_data[0] == student_id:
                    found = True
                    print(f"Course: {grade_data[1]}, Grade: {grade_data[2]}")
            if not found:
                print("No grades found for this student.")
    else:
        print("Grades data is unavailable.")


def view_student_information():
    """View detailed information for a specific studnet from student.txt"""
    student_id = input("Enter student ID: ")
    print(f"\n--- Information for Student ID {student_id} ---")

    if STUDENTS_FILE:
        with open(STUDENTS_FILE, 'r') as f:
            found = False
            for line in f:
                student_data = line.strip().split(",")
                if student_data[0] == student_id:
                    found = True
                    print(f"ID: {student_data[0]}, Name: {student_data[1]}, Program: {student_data[2]}")
                    break
            if not found:
                print("Student not found.")
    else:
        print("Student data is unavailable.")
