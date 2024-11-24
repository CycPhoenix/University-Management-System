from utils.display_choices import display_choices
from utils.load_data import load_data


# Constants for file paths
COURSES_FILE = 'data/courses.txt'
LECTURERS_FILE = 'data/lecturers.txt'
LECTURER_COURSES_FILE = 'data/lecturer_courses.txt'
STUDENTS_FILE = 'data/students.txt'

DEPARTMENTS_FILE = 'data/departments.txt'
FOUNDATION_FILE = 'data/courses/foundation.txt'
DIPLOMA_FILE = 'data/courses/diploma.txt'
UNDERGRADUATE_DIR = 'data/courses/undergraduate/'
POSTGRADUATE_DIR = 'data/courses/postgraduate/'

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
