from utils.display_choices import display_choices
from utils.load_data import load_data
from utils.write_data import write_data
from settings import LECTURERS_FILE


def view_all_lecturer():
    """View all lecturers in the system."""
    print("\n--- View All Lecturers ---")

    try:
        lecturers = load_data(LECTURERS_FILE)
        if not lecturers:
            print("No lecturers found. Please add lecturers first.")
            return
    except FileNotFoundError:
        print(f"Error: File '{LECTURERS_FILE}' not found.")
        return
    except Exception as e:
        print(f"Error: Failed to load lecturers. {e}")
        return
    
    print("\n-- List of Lecturersw ---")
    for lecturer in lecturers:
        print(lecturer.strip())
