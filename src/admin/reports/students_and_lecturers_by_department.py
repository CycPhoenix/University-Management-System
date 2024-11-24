from utils.load_data import load_data
from settings import STUDENTS_FILE, LECTURERS_FILE, DEPARTMENTS_FILE

def students_and_lecturers_by_department():
    """Generate breakdown of students and lecturers by department."""
    try:
        departments = load_data(DEPARTMENTS_FILE)
        students = load_data(STUDENTS_FILE)
        lecturers = load_data(LECTURERS_FILE)

        print("\n--- Students and Lecturers by Department ---")
        for department in departments:
            department = department.strip()
            student_count = sum(1 for student in students if department in student)
            lecturer_count = sum(1 for lecturer in lecturers if department in lecturer)
            print(f"{department}: {student_count} Students, {lecturer_count} Lecturers")
        print("\nReport generated successfully!")

    except FileNotFoundError as e:
        print(f"Error: Missing file - {e}")
    except Exception as e:
        print(f"Error: Failed to generate report - {e}")
