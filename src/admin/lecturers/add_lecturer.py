import os
from utils.append_data import append_data
from utils.load_data import load_data
from settings import LECTURERS_FILE, DEPARTMENTS_FILE

def add_lecturer():
    """Add a new lecturer to the system."""
    al_art = r"""
     ___    _    _   _               _                          
    | . | _| | _| | | |   ___  ___ _| |_ _ _  _ _  ___  _ _ 
    |   |/ . |/ . | | |_ / ._>/ | ' | | | | || '_>/ ._>| '_>
    |_|_|\___|\___| |___|\___.\_|_. |_| `___||_|  \___.|_|  
    """
    separator_length = max(len(line) for line in al_art.splitlines())
    separator = "=" * separator_length

    while True:
        print()
        print(separator)
        print(al_art)
        print(separator)

        # Input Lecturer ID
        lecturer_id = input("Enter the lecturer ID (or type 'Cancel' to exit): ").strip().upper()
        if lecturer_id.lower() == 'cancel':
            print("Action canceled. Returning to manage lecturers menu.")
            return
        if not lecturer_id:
            print("Lecturer ID cannot be empty. Please try again.")
            continue

        # Check if lecturer ID already exists
        try:
            existing_lecturers = load_data(LECTURERS_FILE)
            if any(lecturer_id in line.split(',')[0] for line in existing_lecturers):
                print("Lecturer ID already exists. Please enter a new ID.")
                continue
        except FileNotFoundError:
            pass # If the file does not exist, treat it as empty
        break

    # Input Lecturer Name   
    lecturer_name = input("Enter the lecturer name (or type 'Cancel' to exit): ").strip()
    if lecturer_name.lower() == 'cancel':
        print("Action canceled. Returning to manage lecturers menu.")
        return
    if not lecturer_name:
        print("Lecturer name cannot be empty.")
        return

    # Select Department
    try:
        departments = load_data(DEPARTMENTS_FILE)
        if not departments:
            print("No departments found. Please ensure departments.txt is populated.")
            return

        print("\n--- Available Departments ---")
        for idx, department in enumerate(departments, start=1):
            print(f"{idx}.  {department.strip()}")

        while True:
            department_choice = input("Select a department: ").strip()
            if department_choice.isdigit() and 1 <= int(department_choice) <= len(departments):
                selected_department = departments[int(department_choice) - 1].strip()
                break
            else:
                print("Invalid choice. Please enter a valid number corresponding to a department.")
                
    except FileNotFoundError:
        print(f"Error: File '{DEPARTMENTS_FILE}' not found.")
        return

    # Input Additional Details
    email = input("Enter the lecturer email (optional, press Enter to skip): ").strip()
    if not email:
        email = "N/A"
    contact_number = input("Enter the lecturer contact number (optional, press Enter to skip): ").strip()
    if not contact_number:
        contact_number = "N/A"

    # Confirm and Save Lecturer
    lecturer_details = f"{lecturer_id},{lecturer_name},{selected_department},{email},{contact_number}"
    try:
        append_data(LECTURERS_FILE, lecturer_details)
        print(f"Lecturer '{lecturer_name}' added successfully!")
    except Exception as e:
        print(f"Error: Failed to add lecturer. {e}")
