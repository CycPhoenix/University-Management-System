from utils.display_choices import display_choices
from utils.load_data import load_data
from utils.write_data import write_data
from settings import STUDENTS_FILE


def remove_student():
    """Remove a student from the system."""
    print("\n--- Remove Student ---")

    # Load existing students
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
    
    # Display students and select one to remove
    student_options = {str(i + 1): student for i, student in enumerate(students)}
    student_options[str(len(students) + 1)] = 'Cancel'

    print("\n--- Existing Students ---")
    for idx, student in student_options.items():
        if idx != str(len(students) + 1):
            print(f"{idx}. {student.strip()}")

    choice = input(f"\nSelect a student to remove (1-{len(students)}) or type '{len(students) + 1}' to cancel: ").strip()
    if choice == str(len(students) + 1):
        print("Action canceled. Returning to manage students menu.")
        return
    
    if choice not in student_options:
        print("Invalid choice. Please try again.")
        return
    
    selected_student = student_options[choice]
    print(f"Selected student: {selected_student.strip()}")

    # Confirm removal
    confirmation = input(f"Are you sure you want to remove '{selected_student.strip()}'? (yes/no): ").strip().lower()
    if confirmation != 'yes':
        print("Action canceled. Returning to manage students menu.")
        return
    
    # Update students file
    try:
        with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
            for student in students:
                if student != selected_student:
                    f.write(f"{student.strip()}\n")
        print(f"Student '{selected_student.strip()}' removed successfully!")
    except Exception as e:
        print(f"Error: Failed to remove student. {e}")
