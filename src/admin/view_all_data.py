import os
from utils.load_data import load_data
from settings import STUDENTS_FILE, LECTURERS_FILE, FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR

def view_all_data():
    """View all data in the system."""
    print("\n--- View All Data ---")
    vad_art = r"""
     _ _  _               ___  _  _   ___        _           
    | | |<_> ___  _ _ _  | . || || | | . \ ___ _| |_ ___ 
    | ' || |/ ._>| | | | |   || || | | | |<_> | | | <_> |
    |__/ |_|\___.|__/_/  |_|_||_||_| |___/<___| |_| <___|
    """

    separator_length =  max(len(line) for line in vad_art.splitlines())
    separator = "=" * separator_length

    print()
    print(separator)
    print(vad_art)
    print(separator)

    try:
        # Display Students
        display_students()

        # Display Lecturers
        display_lecturers()

        # Display Courses
        display_courses()

    except Exception as e:
        print(f"Error Failed to load data. {e}")

def display_students():
    """Display all students."""
    print("\n--- Students ---")
    student_col_widths = [15, 25, 25, 100, 30, 15]
    student_headers = ['ID', 'Name', 'Department', 'Program', 'Email', 'Contact']
    display_table(STUDENTS_FILE, student_headers, student_col_widths)

def display_lecturers():
    """Display all lecturers."""
    print("\n--- Lecturers ---")
    lecturer_col_widths = [15, 25, 25, 30, 15]
    lecturer_headers = ['ID', 'Name', 'Department', 'Email', 'Contact']
    display_table(LECTURERS_FILE, lecturer_headers, lecturer_col_widths)

def display_courses():
    """Display all courses."""
    print("\n--- Courses ---")
    course_col_widths = [25, 110, 10]
    course_headers = ['Code', 'Name', 'Credits']

    # Foundation Courses
    print("\n--- Foundation Courses ---")
    display_table(FOUNDATION_FILE, course_headers, course_col_widths)

    # Diploma Courses
    print("\n--- Diploma ---")
    display_table(DIPLOMA_FILE, course_headers, course_col_widths)

    # Undergraduate Courses
    print("\n--- Undergraduate Courses ---")
    display_folder_courses(UNDERGRADUATE_DIR, course_headers, course_col_widths)

    # Postgraduate Courses
    print("\n--- Postgraduate Courses ---")
    display_folder_courses(POSTGRADUATE_DIR, course_headers, course_col_widths)

def display_table(file_path, headers, col_width):
    """Display data from a single file in a tabular format."""
    try:
        data = load_data(file_path)
        if not data:
            print("No data available.")
            return
        
        header_row = "".join(f"{header:<{width}}" for header, width in zip(headers, col_width))
        separator = "=" * len(header_row)
        indent = '   '
        
        print(separator)
        print(indent + header_row)
        print(separator)
        for idx, line in enumerate(data, start=1):
            fields = line.strip().split(',')
            if len(fields) == len(headers):
                row = "".join(f"{field.strip():<{width}}" for field, width in zip(fields, col_width))
                print(f"{idx:<3}{row}")
            else:
                print(f"{idx:<3}[Corrupted Data] - {line.strip()}")
        print(separator)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def display_folder_courses(folder_path, headers, col_width):
    """Display courses from all files in a folder."""
    try:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            print(f"\nCategory: {file_name.replace('.txt', '').replace('_', ' ').title()}")
            display_table(file_path, headers, col_width)
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
    except Exception as e:
        print(f"Error: {e}")