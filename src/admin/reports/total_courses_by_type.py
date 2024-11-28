import os
from utils.load_data import load_data
from settings import FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR

def total_courses_by_type():
    """Count the total number of courses by type."""
    # print("\n--- Total Courses by Type ---")
    
    # Art for Total Courses by Type
    tct_art = r"""
     ___       _        _   ___                               _          ___                   
    |_ _|___ _| |_ ___ | | |  _> ___  _ _  _ _  ___ ___  ___ | |_  _ _  |_ _|_ _  ___  ___ 
     | |/ . \ | | <_> || | | <__/ . \| | || '_><_-</ ._><_-< | . \| | |  | || | || . \/ ._>
     |_|\___/ |_| <___||_| `___/\___/`___||_|  /__/\___./__/ |___/`_. |  |_|`_. ||  _/\___.
                                                                  <___'     <___'|_|       
    """

    course_types = {
        'Foundation': FOUNDATION_FILE,
        'Diploma': DIPLOMA_FILE,
        'Undergraduate': UNDERGRADUATE_DIR,
        'Postgraduate': POSTGRADUATE_DIR
    }

    total_courses = []

    # Process each course type
    try:
        for course_type, path in course_types.items():
            if course_type in ['Undergraduate', 'Postgraduate']:
                # For directories , gather courses from all sub files
                course_count = 0
                for file in os.listdir(path):
                    file_path = os.path.join(path, file)
                    courses = load_data(file_path)
                    course_count += len(courses)
                total_courses.append((course_type, course_count))
            else:
                # For single files
                courses = load_data(path)
                total_courses.append((course_type, len(courses)))
    except FileNotFoundError as e:
        print(f"Error: File or directory not found. {e}")
        return
    except Exception as e:
        print(f"Error: Failed to calculate total courses. {e}")
        return
    header_row = f"{'Course Type':<20}{'Total':<15}"
    separator = "=" * len(FOUNDATION_FILE)
    print(separator)
    print(tct_art)
    print(separator)
    print(header_row)
    print(separator)
    for course_type, count in total_courses:
        print(f"{course_type:<20}{count:<15}")
    print(separator)