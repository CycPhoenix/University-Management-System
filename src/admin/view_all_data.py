from utils.load_data import load_data
from settings import STUDENTS_FILE, LECTURERS_FILE, FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR
import os

def view_all_data():
    """View all data in the system."""
    print("\n--- View All Data ---")

    try:
        # Load students and lecturers
        students = load_data(STUDENTS_FILE)
        lecturers = load_data(LECTURERS_FILE)

        print("\n--- Students ---")
        if students:
            for student in students:
                print(student.strip())
        else:
            print("No students found.")

        print("\n--- Lecturers ---")
        if lecturers:
            for lecturer in lecturers:
                print(lecturer.strip())
        else:
            print("No lecturers found.")

        # Load courses
        print("\n--- Courses ---")
        foundation_courses = load_data(FOUNDATION_FILE)
        diploma_courses = load_data(DIPLOMA_FILE)
        undergraduate_courses = [
            (file, load_data(os.path.join(UNDERGRADUATE_DIR, file)))
            for file in os.listdir(UNDERGRADUATE_DIR) if file.endswith(".txt")
        ]
        postgraduate_courses = [
            (file, load_data(os.path.join(POSTGRADUATE_DIR, file)))
            for file in os.listdir(POSTGRADUATE_DIR) if file.endswith(".txt")
        ]

        print("Foundation Courses:")
        if foundation_courses:
            for course in foundation_courses:
                print(course.strip())
        else:
            print("No foundation courses found.")

        print("Diploma Courses:")
        if diploma_courses:
            for course in diploma_courses:
                print(course.strip())
        else:
            print("No diploma courses found.")

        print("Undergraduate Courses:")
        for category, courses in undergraduate_courses:
            print(f"\nCategory: {category}")
            for course in courses:
                print(course.strip())

        print("Postgraduate Courses:")
        for category, courses in postgraduate_courses:
            print(f"\nCategory: {category}")
            for course in courses:
                print(course.strip())
    except Exception as e:
        print(f"Error: Failed to load data. {e}")
