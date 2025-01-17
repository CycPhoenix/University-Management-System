import os
from utils.load_data import load_data
from settings import ASSIGNED_MODULES_FILE, LECTURERS_FILE

def view_assigned_modules():
    """Displays the modules assigned to the current lecturer."""
    print("\n--- View Assigned Modules ---")

    # Validate Lecturer ID
    lecturer_id = input("Enter your Lecturer ID: ").strip().upper()
    try:
        lecturers = load_data(LECTURERS_FILE)
        if not lecturers:
            print("No lecturers found. Please ensure lecturers.txt is populated.")
            return

        # Validate lecturer entry
        valid_lecturers = [lecturer.split(',') for lecturer in lecturers if len(lecturer.split(',')) >= 3]
        if not any(lecturer_id == lecturer[0].strip() for lecturer in valid_lecturers):
            print(f"Lecturer ID '{lecturer_id}' not found. Please try again.")
            return
    except FileNotFoundError:
        print(f"Error: '{LECTURERS_FILE}' not found.")
        return

    # Retrieve Assigned Modules
    try:
        assigned_modules = load_data(ASSIGNED_MODULES_FILE)
        if not assigned_modules:
            print(f"No modules have been assigned to any lecturer yet.")
            return

        lecturer_modules = [
            module.strip().split(',') for module in assigned_modules if module.strip().split(',')[2] == lecturer_id
        ]

        if not lecturer_modules:
            print(f"No modules assigned to Lecturer ID '{lecturer_id}'.")
            return

        # Display Assigned Modules
        print(f"\nModules Assigned to Lecturer ID '{lecturer_id}':")
        print(f"{'Module ID':<15}{'Module Name':<40}")
        print("=" * 55)
        for module in lecturer_modules:
            mod_id, mod_name, _ = module
            print(f"{mod_id:<15}{mod_name:<40}")
    except FileNotFoundError:
        print(f"Error: '{ASSIGNED_MODULES_FILE}' not found.")
    except Exception as e:
        print(f"Error retrieving modules: {e}")
