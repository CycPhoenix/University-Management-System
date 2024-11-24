from utils.load_data import load_data
from settings import FOUNDATION_FILE, DIPLOMA_FILE, UNDERGRADUATE_DIR, POSTGRADUATE_DIR


def total_courses_by_type():
    """Generate total courses by type."""
    try:
        foundation_courses = len(load_data(FOUNDATION_FILE))
        diploma_courses = len(load_data(DIPLOMA_FILE))
        undergraduate_courses = sum(
            len(load_data(f"{UNDERGRADUATE_DIR}{file.strip()}"))
            for file in ['accounting_banking_finance_actuarial.txt',
                        'business_management_marketing_tourism.txt',
                        'computing_technology.txt',
                        'creative_design_multimedia.txt',
                        'design_advertising_animation_vfx.txt',
                        'engineering.txt',
                        'media_international_relations_psychology.txt']
        )
        postgraduate_courses = sum(
            len(load_data(f"{POSTGRADUATE_DIR}{file.strip()}"))
            for file in ['masters.txt', 'phd.txt']
        )

        print("\n--- Total Courses by Type ---")
        print(f"Foundation Courses: {foundation_courses}")
        print(f"Diploma Courses: {diploma_courses}")
        print(f"Undergraduate Courses: {undergraduate_courses}")
        print(f"Postgraduate Courses: {postgraduate_courses}")
        print("\nReport generated successfully!")

    except FileNotFoundError as e:
        print(f"Error: Missing file - {e}")
    except Exception as e:
        print(f"Error: Failed to generate report - {e}")
