from utils.load_data import load_data
from settings import STUDENTS_FILE, LECTURERS_FILE, FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR
import os

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
        """Student"""
        # Calculate student column widths dynamically
        student_col_widths = [15, 25, 25, 30, 15]
        student_headers = ['ID', 'Name', 'Departments', 'Email', 'Contact']

        student_header_row = "".join(f"{header:<{width}}" for header, width in zip(student_headers, student_col_widths))
        separator = "=" * len(student_header_row)

        # Add indentation 
        indent = '   ' # Add 3 spaces of indentation

        # Load students
        students = load_data(STUDENTS_FILE)

        # Parse view all students into fields
        student_data = []
        for student in students:
            student_fields = student.strip().split(',')
            if len(student_fields) == 5:
                student_data.append(student_fields)
            else:
                student_data.append(["[Corrupted Data]"])
        print("\n--- Students ---")
        print(separator)
        print(indent + student_header_row)
        print(separator)
        for idx, student_fields in enumerate(student_data, start=1):
            if len(student_fields) == 5:
                row = "".join(f"{field:<{width}}" for field, width in zip(student_fields, student_col_widths))
                print(f"{idx:<3}{row}")
            else:
                print(f"{idx:<3}[Corrupted Data]")
        print(separator)

        """Lecturer"""
        # Calculate lecturer column widths dynamically
        lecturer_col_widths = [15, 25, 25, 30, 15]
        lecturer_headers = ['ID', 'Name', 'Departments', 'Email', 'Contact']

        lecturer_header_row = "".join(f"{header:<{width}}" for header, width in zip(lecturer_headers, lecturer_col_widths))
        separator = "=" * len(lecturer_header_row)

        # Load lecturers
        lecturers = load_data(LECTURERS_FILE)

        # Parse view all lecturers into fields
        lecturer_data = []
        for lecturer in lecturers:
            lecturer_fields = lecturer.strip().split(',')
            if len(lecturer_fields) == 5:
                lecturer_data.append(lecturer_fields)
            else:
                lecturer_data.append(["[Corrupted Data]"])
        print("\n--- Lecturers ---")
        print(separator)
        print(indent + lecturer_header_row)
        print(separator)
        for idx, lecturer_fields in enumerate(lecturer_data, start=1):
            if len(lecturer_fields) == 5:
                row = "".join(f"{field:<{width}}" for field, width in zip(lecturer_fields, lecturer_col_widths))
                print(f"{idx:<3}{row}")
            else:
                print(f"{idx:<3}[Corrupted Data]")
        print(separator)

        """Course"""
        # Calculate course column widths dynamically
        course_col_widths = [25, 110, 10]
        course_headers = ['Code', 'Name', 'Credits']

        # Load courses
        foundations = load_data(FOUNDATION_FILE)
        diplomas = load_data(DIPLOMA_FILE)
        undergraduates = [
            (file, load_data(os.path.join(UNDERGRADUATE_DIR, file)))
            for file in os.listdir(UNDERGRADUATE_DIR) if file.endswith(".txt")
        ]
        postgraduates = [
            (file, load_data(os.path.join(POSTGRADUATE_DIR, file)))
            for file in os.listdir(POSTGRADUATE_DIR) if file.endswith(".txt")
        ]

        course_header_row = "".join(f"{header:<{width}}" for header, width in zip(course_headers, course_col_widths))
        separator = "=" * len(course_header_row)

        # Parse view all courses into fields
        # Foundation Courses
        foundation_data = []
        for foundation in foundations:
            foundation_fields = foundation.strip().split(',')
            if len(foundation_fields) == 3:
                foundation_data.append(foundation_fields)
            else:
                foundation_data.append(["[Corrupted Data]"])
        print("\n--- Foundation Courses ---")
        print(separator)
        print(indent + course_header_row)
        print(separator)
        for idx, foundation_fields in enumerate(foundation_data, start=1):
            if len(foundation_fields) == 3:
                row = "".join(f"{field:<{width}}" for field, width in zip(foundation_fields, course_col_widths))
                print(f"{idx:<3}{row}")
            else:
                print(f"{idx:<3}[Corrupted Data]")
        print(separator)
        
        # Diploma Courses
        diploma_data = []
        for diploma in diplomas:
            diploma_fields = diploma.strip().split(',')
            if len(diploma_fields) == 3:
                diploma_data.append(diploma_fields)
            else:
                diploma_data.append(["[Corrupted Data]"])
        print("\n--- Diploma Courses ---")
        print(separator)
        print(indent + course_header_row)
        print(separator)
        for idx, diploma_fields in enumerate(diploma_data, start=1):
            if len(diploma_fields) == 3:
                row = "".join(f"{field:<{width}}" for field, width in zip(diploma_fields, course_col_widths))
                print(f"{idx:<3}{row}")
            else:
                print(f"{idx:<3}[Corrupted Data]")
        print(separator)

        # Undergraduate Courses
        print("\n--- Undergraduate Courses --- ")
        for f, undergraduate_courses in undergraduates:
            print(f"\nCourse: {f.replace('.txt', '').replace('_', ' ').title()}")
            print(separator)
            print(indent + course_header_row)
            print(separator)
            undergraduate_data = []
            for undergraduate in undergraduate_courses:
                undergraduate_fields = undergraduate.strip().split(',')
                if len(undergraduate_fields) == 3:
                    undergraduate_data.append(undergraduate_fields)
                else:
                    undergraduate_data.append("[Corrupted Data]")
            for idx, undergraduate_fields in enumerate(undergraduate_data, start=1):
                if len(undergraduate_fields) == 3:
                    row = row = "".join(f"{field:<{width}}" for field, width in zip(undergraduate_fields, course_col_widths))
                    print(f"{idx:<3}{row}")
                else:
                    print(f"{idx:<3}[Corrupted Data]")
            print(separator)

        # Postgraduate Courses
        print("\n--- Postgraduate Courses --- ")
        for f, postgraduate_courses in postgraduates:
            print(f"\nCourse: {f.replace('.txt', '').replace('_', ' ').title()}")
            print(separator)
            print(indent + course_header_row)
            print(separator)
            postgraduate_data = []
            for postgraduate in postgraduate_courses:
                postgraduate_fields = postgraduate.strip().split(',')
                if len(undergraduate_fields) == 3:
                    postgraduate_data.append(undergraduate_fields)
                else:
                    postgraduate_data.append("[Corrupted Data]")
            for idx, postgraduate_fields in enumerate(postgraduate_data, start=1):
                if len(undergraduate_fields) == 3:
                    row = row = "".join(f"{field:<{width}}" for field, width in zip(postgraduate_fields, course_col_widths))
                    print(f"{idx:<3}{row}")
                else:
                    print(f"{idx:<3}[Corrupted Data]")
            print(separator)
    except Exception as e:
        print(f"Error: Failed to load data. {e}")
