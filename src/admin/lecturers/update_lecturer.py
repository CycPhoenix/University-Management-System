from utils.load_data import load_data
from utils.write_data import write_data
from settings import LECTURERS_FILE

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

    print("\n--- Existing Lecturers ---")
    for idx, lecturer in enumerate(lecturers, start=1):
        print(f"{idx}. {lecturer.strip()}")
    print(f"{len(lecturers) + 1}. Cancel")

    choice = input(f"\nSelect a lecturer to update (1-{len(lecturers)}) or type '{len(lecturers) + 1}' to cancel: ").strip().upper()
    if not choice.isdigit() or not (1 <= int(choice) <= len(lecturers) + 1):
        print("Invalid choice. Returning to manage lecturers menu.")
        return

    if int(choice) == len(lecturers) + 1:
        print("Action canceled. Returning to manage students menu.")
        return

    selected_lecturer = lecturers[int(choice) - 1]
    lecturer_fields = selected_lecturer.split(',')
    if len(lecturer_fields) != 5:
        print("Error: Selected lecturer data is corrupted.")
        return
    
    lecturer_id, lecturer_name, department, email, contact_number = [field.strip() for field in lecturer_fields]

    # Update fields
    new_id = input(f"Enter new Lecturer ID (press Enter to keep '{lecturer_id}'): ").strip() or lecturer_id
    new_name = input(f"Enter new Name (press Enter to keep '{lecturer_name}'): ").strip() or lecturer_name
    new_department = input(f"Enter new Department (press Enter to keep '{department}'): ").strip() or department
    new_email = input(f"Enter new Email (press Enter to keep '{email}'): ").strip() or email
    new_contact_number = input(f"Enter new Contact Number (press Enter to keep '{contact_number}'): ").strip() or contact_number

    # Combine updated fields
    updated_lecturer = f"{new_id},{new_name},{new_department},{new_email},{new_contact_number}"

    # Write updated data to the file
    try:
        updated_lecturers = [updated_lecturer if lecturer.strip() == selected_lecturer else lecturer.strip() for lecturer in lecturers]
        write_data(LECTURERS_FILE, updated_lecturers)
        print(f"Lecturer '{new_name}' updated successfully!")
    except Exception as e:
        print(f"Error: Failed to update lecturer. {e}")
