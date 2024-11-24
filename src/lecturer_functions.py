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
GRADES_FILE = get_resource_path('data/grades.txt')
ENROLLMENTS_FILE = get_resource_path('data/enrollments.txt')
ATTENDANCE_FILE = get_resource_path('data/attendance.txt')


def lecturer_menu():
    """
    Menu for Lecturer functions.
    Prompts the lecturer to enter their ID and provides access to various functionalities.
    """
    lecturer_id = input("Enter your Lecturer ID: ").strip()
    if not lecturer_exists(lecturer_id):
        print("Lecturer ID not found. Please contact the administrator.")
        
    while True:
        print("\n--- Lecturer Menu ---")
        print("1. View Assigned Modules")
        print("2. Record Grades")
        print("3. View Students in a Module")
        print("4. Mark Attendance")
        print("5. View Attendance for a Module")
        print("6. View Student Grades")
        print("7. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            view_assigned_modules(lecturer_id)
        elif choice == "2":
            record_grade()
        elif choice == "3":
            view_students_in_course()
        elif choice == "4":
            mark_attendance()
        elif choice == "5":
            view_attendance()
        elif choice == "6":
            view_student_grades()
        elif choice == "7":
            break
        else:
            print("Invalid option. Please try again.")

def lecturer_exists(lecturer_id):
    """
    Checks if a lecturer exists in lecturers.txt.
    
    Parameters:
    - lecturer_id (str): ID of the lecturer.
    
    Returns:
    - bool: True if lecturer exists, False otherwise.
    """
    if not LECTURERS_FILE:
        return False
    with open(LECTURERS_FILE, 'r') as f:
        for line in f:
            existing_id = line.strip().split(",")[0]
            if existing_id == lecturer_id:
                return True
    return False

def view_assigned_modules(lecturer_id):
    """
    Displays a list of modules assigned to the lecturer.

    Parameters:
    - lecturer_id (str): ID of the lecturer.
    
    Returns:
    - None
    """
    if not LECTURER_COURSES_FILE:
        print("No module assignments found.")
        return

    assigned_courses = []
    with open(LECTURER_COURSES_FILE, 'r') as f:
        for line in f:
            current_lecturer_id, course_code = line.strip().split(",")
            if current_lecturer_id == lecturer_id:
                assigned_courses.append(course_code)
    if not assigned_courses:
        print("No modules assigned to you.")
        return
    
    print("\n--- Assigned Modules ---")
    with open(COURSES_FILE, 'r') as f:
        courses = f.readlines()
        for course in courses:
            course_code, course_name, credits = course.strip().split(",")
            if course_code in assigned_courses:
                print(f"Code: {course_code}, Name: {course_name}, Credits: {credits}")

def record_grade():
    """
    Records the grade of a student for a particular course.
    
    Returns:
    - None
    """
    student_id = input("Enter Student ID: ").strip()
    course_code = input("Enter Course Code: ").strip()
    grade = input("Enter Grade (e.g., A, B, C): ").strip().upper()

    # Validate grade input
    valid_grades = ['A', 'B', 'C', 'D', 'F']
    if grade not in valid_grades:
        print("Invalid grade entered.")
        return
    
    with open(GRADES_FILE, 'a') as f:
        f.write(f"{student_id}, {course_code}, {grade}\n")
    print("Grade recorded successfully.")

def view_students_in_course():
    """
    Displays a list of students enrolled in a specific course.
    
    Returns:
    - None
    """
    course_code = input("Enter Course Code: ").strip()
    
    if not ENROLLMENTS_FILE:
        print("Enrollments data not found.")
        return
    
    enrolled_students = []
    
    with open(ENROLLMENTS_FILE, 'r') as f:
        students = []
        for line in f:
            student_id, enrolled_course = line.strip().split(",")
            if enrolled_course == course_code:
                enrolled_students.append(student_id)

    if not enrolled_students:
        print(f"No students enrolled in course {course_code}.")
        return
    
    print(f"\n--- Students Enrolled in {course_code} ---")
    with open(STUDENTS_FILE, 'r') as f:
        students = f.readlines()
        for student in students:
            student_id, name, department = student.strip().split(",")
            if student_id in enrolled_students:
                print(f"ID: {student_id}, Name: {name}, Department: {department}")

def mark_attendance():
    """
    Marks attendance for a studnet in a course.
    
    Returns:
    - None
    """
    student_id = input("Enter Student ID: ").strip()
    course_code = input("Enter Course Code: ").strip()
    status = input("Enter Attendance Status (Present/Absent): ").strip().capitalize()

    if status not in ["Present", "Absent"]:
        print("Invalid attendance status entered.")
        return
    
    with open(ATTENDANCE_FILE, 'a') as f:
        f.write(f"{student_id}, {course_code}, {status}\n")
    print("Attendance marked succcessfully.")

def view_attendance():
    """
    Displays attendance records for all students in a course.
    
    Returns:
    - None
    """
    course_code = input("Enter Course Code: ").strip()

    if not ATTENDANCE_FILE:
        print("Attendance data not found")
    
    attendance_records = []
    with open(ATTENDANCE_FILE, 'r') as f:
        for line in f:
            student_id, recorded_course, status = line.strip().split(",")
            if recorded_course == course_code:
                attendance_records.append((student_id, status))
        
    if not attendance_records:
        print(f"No attendance records for course {course_code}.")

    print(f"\n--- Attendance for {course_code} ---")
    for student_id, status in attendance_records:
        print(f"Student ID: {student_id}, Status: {status}")

def view_student_grades():
    """
    Displays grades for students in the lecturer's courses.

    Returns:
    - None
    """
    course_code = input("Enter Course Code: ").strip()

    if not GRADES_FILE:
        print("Grades data not found.")
        return
    
    student_grades = []
    with open(GRADES_FILE, 'r') as f:
        for line in f:
            student_id, record_course, grade = line.strip().split(",")
            if record_course == course_code:
                student_grades.append((student_id, grade))

    if not student_grades:
        print(f"No grades recorded for course {course_code}.")
        return
    
    print(f"\n--- Grades for {course_code} --- ")
    for student_id, grade in student_grades:
        print(f"Student ID: {student_id}, Grade: {grade}")
