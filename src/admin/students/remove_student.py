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
    
    student_data = []
    for student in students:
        student_fields = student.strip().split(',')
        if len(student_fields) == 6:
            student_data.append(student_fields)
        else:
            student_data.append(["[Corrupted Data]"])
    
    # Calculate column widths dynamically
    col_widths = [15, 25, 25, 100, 30, 15]
    headers = ['ID', 'Name', 'Department', 'Program', 'Email', 'Contact']

    # Add indentation
    indent = '   ' # Add 3 spaces of indentation

    header_row = "".join(f"{header:<{width}}" for header, width in zip(headers, col_widths))
    separator = "=" * len(header_row)

    print("--- Existing Students ---")
    print(separator)
    print(indent + header_row)
    print(separator)
    
    for idx, student_fields in enumerate(student_data, start=1):
        if len(student_fields) == 6:
            row = "".join(f"{field:<{width}}" for field, width in zip(student_fields, col_widths))
            print(f"{idx:<3}{row}")
        else:
            print(f"{idx:<3}[Corrupted Data]")
    print(separator)

    while True:
        choice = input(f"\nSelect a student to remove (1-{len(students)}) or type '{len(students) + 1}' to cancel: ").strip()
        if choice.isdigit() or (1 <= int(choice) <= len(students) + 1):
            break
        elif choice == str(len(students) + 1):
            print("Action canceled. Returning to manage students menu.")
            return
        else:
            print("Invalid choice. Please enter a valid number.")
            return

    selected_student = students[int(choice) - 1]
    student_fields = selected_student.split(",") # Split the student's details into fields
    student_id = student_fields[0] if len(student_fields) > 0 else "N/A"
    student_name = student_fields[1] if len(student_fields) > 1 else "N/A"
    student_department = student_fields[2] if len(student_fields) > 2 else "N/A"
    student_email = student_fields[3] if len(student_fields) > 3 else "N/A"
    student_contact = student_fields[4] if len(student_fields) > 4 else "N/A"

    info = f"ID: {student_id} | Name: {student_name} | Department: {student_department} | Email: {student_email} | Contact: {student_contact}"

    # Print selected student details in the desired format
    print(f"Selected student - {info}")

    confirmation = input(f"Are you sure you want to remove '{student_name}'? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Action canceled. Returning to manage students menu.")
        return

    try:
        updated_students = [student for student in students if student != selected_student]
        write_data(STUDENTS_FILE, updated_students)
        print(f"Student '{student_name}' removed successfully!")
    except Exception as e:
        print(f"Error: Failed to remove student. {e}")
