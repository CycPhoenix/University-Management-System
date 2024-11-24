from utils.load_data import load_data
from .total_overview import total_overview
from .students_and_lecturers_by_department import students_and_lecturers_by_department
from .total_courses_by_type import total_courses_by_type


def generate_reports():
    """Menu for generating reports."""
    while True:
        print("\n--- Generate Reports ---")
        print("1. Generate Total Overview")
        print("2. Students and Lecturers by Department")
        print("3. Total Courses by Type")
        print("4. Back to Admin Menu")
        choice = input("Select an option: ").strip()

        try:
            if choice == "1":
                total_overview()
            elif choice == "2":
                students_and_lecturers_by_department()
            elif choice == "3":
                total_courses_by_type()
            elif choice == "4":
                print("Returning to admin menu...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred while generating the report: {e}")
