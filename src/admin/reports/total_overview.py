from utils.load_data import load_data
from settings import (
    STUDENTS_FILE,
    LECTURERS_FILE,
    FOUNDATION_FILE,
    DIPLOMA_FILE,
    UNDERGRADUATE_DIR,
    POSTGRADUATE_DIR
)


def total_overview():
    """Generate total overview of students, lecturers and courses."""
    try:
        students = load_data(STUDENTS_FILE)
        lecturers = load_data(LECTURERS_FILE)
        total_courses = 0
        
        # Count courses in each category
        foundation_courses = len(load_data(FOUNDATION_FILE))
        diploma_courses = len(load_data(DIPLOMA_FILE))
        undergraduate_courses = sum(
            len(load_data(f"{UNDERGRADUATE_DIR}{file.strip()}"))
            for file in [
                'accounting_banking_finance_actuarial.txt',
                'business_management_marketing_tourism.txt',
                'computing_technology.txt',
                'creative_design_multimedia.txt',
                'design_advertising_animation_vfx.txt',
                'engineering.txt',
                'media_international_relations_psychology.txt'
            ]
        )
        postgraduate_courses = sum(
            len(load_data(f"{POSTGRADUATE_DIR}{file.strip()}"))
            for file in ['masters.txt', 'phd.txt']
        )

        total_courses = (
            foundation_courses
            + diploma_courses
            + undergraduate_courses
            + postgraduate_courses
        )

        print("\n--- Total Overview ---")
        print(f"Total Students: {len(students)}")
        print(f"Total Lecturers: {len(lecturers)}")
        print(f"Total Courses: {total_courses}")
        print(f"\nReport generated successfully!")

    except FileNotFoundError as e:
        print(f"Error: Missing file - {e}")
    except Exception as e:
        print(f"Error: Failed to generate report - {e}")
