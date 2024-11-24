from utils.display_choices import display_choices
from utils.load_data import load_data
from utils.write_data import write_data
from settings import LECTURERS_FILE, DEPARTMENTS_FILE


def add_lecturer():
    """Add a new lecturer to the system."""
    print("\n--- Add New Lecturer ---")

    # Input Lecturer ID
    while True:
        lecturer_id = input("Enter the lecturer ID (or type 'Cancel' to exit): ").strip()
        if lecturer_id.lower() == 'cancel':
            print("Action canceled. Returning to manage lecturers menu.")
            return
        if lecturer_id == '':
            print("Lecturer ID cannot be empty. Please try again.")
            continue

        # Check if lecturer ID already exists
        existing_lecturer = load_data(LECTURERS_FILE)
        if any(lecturer_id.lower() == line.split(',')[0].strip().lower() for line in existing_lecturer):
            print(f"Lecturer ID '{lecturer_id}' already exists. Please enter a new ID.")
            continue
        break

    # Input Lecturer Name
    lecturer_name = input("Enter the lecturer name (or type 'Cancel' to exit): ").strip()
    if lecturer_name.lower() == 'cancel':
        print("Action canceled. Returning to manage lecturers menu.")
        return
    if lecturer_name == '':
        print("Lecturer name cannot be empty.")
        return
    
    # Select Department
    try:
        departments = [dep.strip() for dep in load_data(DEPARTMENTS_FILE)]
        if not departments:
            print("No departments found. Please ensure departments.txt is populated.")
            return
        department = display_choices({str(i + 1): dep for i, dep in enumerate(departments)})
    except FileNotFoundError:
        print(f"Error: File '{DEPARTMENTS_FILE}' not found.")
        return
    
    # Input Addisional Details
    email = input("Enter the lecturer email (optional, press Enter to skip): ").strip()
    contact_number = input("Enter the lecturer contact number (optional, press Enter to skip): ").strip()

    # Confirm and Save Lecturer
    lecturer_details = f"{lecturer_id},{lecturer_name},{department},{email},{contact_number}"
    try:
        write_data(LECTURERS_FILE, lecturer_details)
        print(f"Lecturer '{lecturer_name}' added successfully!")
    except Exception as e:
        print(f"Error: Failed to add lecturer. {e}")
