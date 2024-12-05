from utils.load_data import load_data
from utils.write_data import write_data
from settings import STUDENTS_FILE

def update_student():
    """Update a student's details."""
    us_art = r"""
     _ _         _        _         ___    _          _             _      
    | | | ___  _| | ___ _| |_ ___  / __> _| |_ _ _  _| | ___ ._ _ _| |_ 
    | ' || . \/ . |<_> | | | / ._> \__ \  | | | | |/ . |/ ._>| ' | | |  
    `___'|  _/\___|<___| |_| \___. <___/  |_| `___|\___|\___.|_|_| |_|  
         |_|                                                            
    """
    separator_length = max(len(line) for line in us_art.splitlines())
    separator = "=" * separator_length

    print()
    print(separator)
    print(us_art)
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

    choice = input(f"\nSelect a student to update (1-{len(students)}) or type '{len(students) + 1}' to cancel: ").strip().upper()
    if not choice.isdigit() or not (1 <= int(choice) <= len(students) + 1):
        print("Invalid choice. Returning to manage students menu.")
        return

    if int(choice) == len(students) + 1:
        print("Action canceled. Returning to manage students menu.")
        return

    selected_student = students[int(choice) - 1]
    student_fields = selected_student.split(',')
    if len(student_fields) != 5:
        print("Error: Selected student data is corrupted.")
        return

    student_id, student_name, department, email, contact_number = [field.strip() for field in student_fields]

    # Update fields
    new_id = input(f"Enter new Student ID (press Enter to keep '{student_id}'): ").strip().upper() or student_id
    new_name = input(f"Enter new Name (press Enter to keep '{student_name}'): ").strip() or student_name
    new_department = input(f"Enter new Department (press Enter to keep '{department}'): ").strip() or department
    new_email = input(f"Enter new Email (press Enter to keep '{email}'): ").strip() or email
    new_contact_number = input(f"Enter new Contact Number (press Enter to keep '{contact_number}'): ").strip() or contact_number

    # Combine updated fields
    updated_student = f"{new_id},{new_name},{new_department},{new_email},{new_contact_number}"

    # Write updated data to the file
    try:
        updated_students = [updated_student if student == selected_student else student for student in students]
        write_data(STUDENTS_FILE, updated_students)
        print(f"Student '{new_name}' updated successfully!")
    except Exception as e:
        print(f"Error: Failed to update student. {e}")
