import os
from utils.load_data import load_data
from utils.write_data import write_data
from settings import STUDENTS_FILE

def remove_student():
    """Remove a student from the system."""
    rs_art = r"""
     ___                              ___    _          _             _   
    | . \ ___ ._ _ _  ___  _ _  ___  / __> _| |_ _ _  _| | ___ ._ _ _| |_ 
    |   // ._>| ' ' |/ . \| | |/ ._> \__ \  | | | | |/ . |/ ._>| ' | | |  
    |_\_\\___.|_|_|_|\___/|__/ \___. <___/  |_| `___|\___|\___.|_|_| |_|                                       
    """

    separator_length = max(len(line) for line in rs_art.splitlines())
    separator = "=" * separator_length

    print()
    print(separator)
    print(rs_art)
    print(separator)

    # Load existing students
    try:
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found. Please add students first.")
            return
    except FileNotFoundError:
        print(f"Error: File '{STUDENTS_FILE}' not found.")
        return

    print("\n--- Existing Students ---")
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. {student.strip()}")
    print(f"{len(students) + 1}. Cancel")

    choice = input(f"\nSelect a student to remove (1-{len(students)}) or type '{len(students) + 1}' to cancel: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(students) + 1):
        print("Invalid choice. Returning to manage students menu.")
        return

    if int(choice) == len(students) + 1:
        print("Action canceled. Returning to manage students menu.")
        return

    selected_student = students[int(choice) - 1]

    confirmation = input(f"Are you sure you want to remove '{selected_student.strip()}'? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Action canceled. Returning to manage students menu.")
        return

    try:
        updated_students = [student for student in students if student != selected_student]
        write_data(STUDENTS_FILE, updated_students)
        print(f"Student '{selected_student.strip()}' removed successfully!")
    except Exception as e:
        print(f"Error: Failed to remove student. {e}")
