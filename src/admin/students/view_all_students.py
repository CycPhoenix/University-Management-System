from utils.display_choices import display_choices
from utils.load_data import load_data
from utils.write_data import write_data
from settings import STUDENTS_FILE


def view_all_students():
    """View all students in the system."""
    print("\n--- View All Students ---")

    try:
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found. Please add students first.")
            return
    except FileNotFoundError:
        print(f"Error: File '{STUDENTS_FILE}' not found.")
        return
    except Exception as e:
        print(f"Error: Failed to load students. {e}")
        return
    
    print("\n--- List of Students ---")
    for student in students:
        print(student.strip())
