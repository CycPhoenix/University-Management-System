import os
from utils.load_data import load_data
from utils.write_data import write_data
from settings import LECTURERS_FILE, DEPARTMENTS_FILE

def update_lecturer():
    """Update a lecturer's details."""
    ul_art = r"""
     _ _         _        _         _               _                          
    | | | ___  _| | ___ _| |_ ___  | |   ___  ___ _| |_ _ _  _ _  ___  _ _ 
    | ' || . \/ . |<_> | | | / ._> | |_ / ._>/ | ' | | | | || '_>/ ._>| '_>
    `___'|  _/\___|<___| |_| \___. |___|\___.\_|_. |_| `___||_|  \___.|_|  
         |_|                                                               
    """
    separator_length = max(len(line) for line in ul_art.splitlines())
    separator = "=" * separator_length

    print()
    print(separator)
    print(ul_art)
    print(separator)

    # Load existing lecturers
    try:
        lecturers = load_data(LECTURERS_FILE)
        if not lecturers:
            print("No lecturers found. Please add lecturers first.")
            return
    except FileNotFoundError:
        print(f"Error: File '{LECTURERS_FILE}' not found.")
        return

    # Search for the lecturer by ID
    lecturer_id = input("Enter the Lecturer ID to update (or type 'Cancel' to exit): ").strip().upper()
    if lecturer_id.lower() == 'cancel':
        print("Action canceled. Returning to admin menu.")
        return
    
    # Find the lecturer record
    found = False
    updated_lecturers = []
    for line in lecturers:
        lecturer_data = line.strip().split(',')
        if lecturer_data[0] == lecturer_id:
            found = True
            print(f"\nCurrent Details:\nID: {lecturer_data[0]}\nName: {lecturer_data[1]}\nDepartment: {lecturer_data[2]}\nEmail: {lecturer_data[3]}\nContact Number: {lecturer_data[4]}")

            # Update Name
            new_name = input(f"Enter new Name (press Enter to keep current): ").strip() or lecturer_data[1]
            if not new_name:
                new_name = lecturer_data[1]
            
            # Update Department
            try:
                departments = load_data(DEPARTMENTS_FILE)
                if not departments:
                    print("No departments found in departments.txt.")
                    return
                
                print("\n--- Available Departments ---")
                for idx, department in enumerate(departments, start=1):
                    print(f"{idx}. {department.strip()}")
                
                while True:
                    department_choice = input("Select a department (or press Enter to keep current): ").strip()
                    if not department_choice:
                        new_department = lecturer_data[2]
                        break
                    if department_choice.isdigit() and 1 <= int(department_choice) <= len(departments):
                        new_department = departments[int(department_choice) - 1].strip()
                        break
                    else:
                        print("Invalid choice. Please enter a valid number corresponding to a department.")
            except FileNotFoundError:
                print(f"Error: File '{DEPARTMENTS_FILE}' not found.")
                return
            
            while True:
                new_email = input(f"Enter new Email (press Enter to keep current): ").strip() or lecturer_data[3]
                if new_email and "@" not in new_email:
                    print("Invalid email address. Please try again.")
                else:
                    new_email = new_email or "N/A"
                    break
            
            while True:
                new_contact_number = input("Enter new Contact Number (press Enter to keep current): ").strip() or lecturer_data[4]
                if new_contact_number and not new_contact_number.isdigit():
                    print("Invalid contact number. Please enter digits only.")
                if not new_contact_number:
                    new_contact_number = new_contact_number or "N/A"
                    break
            
            # Append updated lecturer data
            updated_lecturers.append(f"{lecturer_data[0]},{new_name},{new_department},{new_email},{new_contact_number}")
        else:
            updated_lecturers.append(line)

    if not found:
        print(f"Lecturer with ID '{lecturer_id}' not found.")
        return

    # Save updated records
    try:
        write_data(LECTURERS_FILE, updated_lecturers)
        print(f"\nLecturer record with ID '{lecturer_id}' updated successfully!")
    except Exception as e:
        print(f"Error: Failed to update lecturer. {e}")
