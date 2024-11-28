import os
from utils.load_data import load_data
from settings import STUDENTS_FILE, LECTURERS_FILE, FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR

def total_overview():
    """Generate a total overview of the system."""
    # print("\n--- Total Overview ---")

    # Art for Total Overview
    to_art = r"""
     ___       _        _   ___                      _                 
    |_ _|___ _| |_ ___ | | | . | _ _  ___  _ _  _ _ <_> ___  _ _ _ 
     | |/ . \ | | <_> || | | | || | |/ ._>| '_>| | || |/ ._>| | | |
     |_|\___/ |_| <___||_| `___'|__/ \___.|_|  |__/ |_|\___.|__/_/ 
    """
    
    header_row = f"{'Category':<30}{'Total':<10}"
    
    # Calculate the separator length based on the longest line in the ASCII art
    separator_length = max(len(line) for line in to_art.splitlines())
    separator = "=" * separator_length

    try:
        students = load_data(STUDENTS_FILE)
        lecturers = load_data(LECTURERS_FILE)

        # Count courses
        foundation_courses = len(load_data(FOUNDATION_FILE))
        diploma_courses = len(load_data(DIPLOMA_FILE))
        undergraduate_courses = sum(len(load_data(os.path.join(UNDERGRADUATE_DIR, file)))
                                    for file in os.listdir(UNDERGRADUATE_DIR) if file.endswith(".txt"))
        postgraduate_courses = sum(len(load_data(os.path.join(POSTGRADUATE_DIR, file)))
                                    for file in os.listdir(POSTGRADUATE_DIR) if file.endswith(".txt"))

        # Display in a formatted table
        print()
        print(separator)
        print(to_art)
        print(separator)
        print(header_row)
        print(separator)
        print(f"{'Total Students':<30}{len(students):<10}")
        print(f"{'Total Lecturers':<30}{len(lecturers):<10}")
        print(f"{'Foundation Courses':<30}{foundation_courses:<10}")
        print(f"{'Diploma Courses':<30}{diploma_courses:<10}")
        print(f"{'Undergraduate Courses':<30}{undergraduate_courses:<10}")
        print(f"{'Postgraduate Courses':<30}{postgraduate_courses:<10}")
        print(separator)

    except Exception as e:
        print(f"Error: Failed to generate overview. {e}")
