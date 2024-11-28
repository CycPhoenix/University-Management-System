from utils.load_data import load_data
from settings import STUDENTS_FILE

def view_all_students():
    """View all students in the system."""
    vas_art = r"""
     _ _  _               ___  _  _   ___    _          _             _       
    | | |<_> ___  _ _ _  | . || || | / __> _| |_ _ _  _| | ___ ._ _ _| |_ 
    | ' || |/ ._>| | | | |   || || | \__ \  | | | | |/ . |/ ._>| ' | | |  
    |__/ |_|\___.|__/_/  |_|_||_||_| <___/  |_| `___|\___|\___.|_|_| |_|  
    """

    # Load students data
    try:
        students = load_data(STUDENTS_FILE)
        if not students:
            print("No students found.")
            return
    except FileNotFoundError:
        print(f"Error: File '{STUDENTS_FILE}' not found.")
        return
    
    # Parse students into fields
    student_data = []
    for student in students:
        student_fields = student.strip().split(',')
        if len(student_fields) == 5:
            student_data.append(student_fields)
        else:
            student_data.append(["[Corrupted Data]"])

    # Calculate column widths dynamically
    col_widths = [15, 25, 25, 30, 15] # Adjust widths as needed
    headers = ['ID', 'Name', 'Department', 'Email', 'Contact']

    # Add indentation
    indent = '   ' # Add 3 spaces of indentation

    # Print header
    header_row = "".join(f"{header:<{width}}" for header, width in zip(headers, col_widths))
    separator = "=" * len(header_row)
    print()
    print(separator)
    print(vas_art)
    print(separator)
    print(indent + header_row)
    print(separator)

    # Print student details
    for idx, student_fields in enumerate(student_data, start=1):
        if len(student_fields) == 5:
            row = "".join(f"{field:<{width}}" for field, width in zip(student_fields, col_widths))
            print(f"{idx:<3}{row}")
        else:
            print(f"{idx:<3}[Corrupted Data]")

    print(separator)
