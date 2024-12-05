import os
from utils.load_data import load_data
from utils.write_data import write_data
from settings import LECTURERS_FILE

def remove_lecturer():
    """Remove a lecturer from the system."""
    rl_art = r"""
     ___                              _               _                          
    | . \ ___ ._ _ _  ___  _ _  ___  | |   ___  ___ _| |_ _ _  _ _  ___  _ _ 
    |   // ._>| ' ' |/ . \| | |/ ._> | |_ / ._>/ | ' | | | | || '_>/ ._>| '_>
    |_\_\\___.|_|_|_|\___/|__/ \___. |___|\___.\_|_. |_| `___||_|  \___.|_|  
    """
    separator_length = max(len(line) for line in rl_art.splitlines())
    separator = "=" * separator_length

    print()
    print(separator)
    print(rl_art)
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

    print("--- Existing Lecturers ---")
    for idx, lecturer in enumerate(lecturers, start=1):
        print(f"{idx}. {lecturer.strip()}")
    print(f"{len(lecturers) + 1}. Cancel")

    while True:
        choice = input(f"\nSelect a lecturer to remove (1-{len(lecturers)}) or type '{len(lecturers) + 1}' to cancel: ").strip()
        if choice.isdigit or (1 <= int(choice) <= len(lecturers) + 1):
            break
        elif choice == str(len(lecturers) + 1):
            print("Action canceled. Returning to manage lecturers menu.")
            return
        else:
            print("Invalid choice. Please enter a valid number.")
            return

    selected_lecturer = lecturers[int(choice) - 1].strip()
    lecturer_fields = selected_lecturer.split(",") # Split the lecturer's details into fields
    lecturer_id = lecturer_fields[0] if len(lecturer_fields) > 0 else "N/A"
    lecturer_name = lecturer_fields[1] if len(lecturer_fields) > 1 else "N/A"
    lecturer_department = lecturer_fields[2] if len(lecturer_fields) > 2 else "N/A"
    lecturer_email = lecturer_fields[3] if len(lecturer_fields) > 3 else "N/A"
    lecturer_contact = lecturer_fields[4] if len(lecturer_fields) > 4 else "N/A"

    info = f"ID: {lecturer_id} | Name: {lecturer_name} | Department: {lecturer_department} | Email: {lecturer_email} | Contact: {lecturer_contact}"

    # Print selected lecturer details in the desired format
    print(f"Selected lecturer - {info}")

    confirmation = input(f"Are you sure you want to remove '{lecturer_name.strip()}'? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Action canceled. Returning to manage lecturers menu.")

    # Write updated list to the file
    try:
        updated_lecturers = [lecturer for lecturer in lecturers if lecturer.strip() != selected_lecturer]
        write_data(LECTURERS_FILE, updated_lecturers)
        print(f"Lecturer '{lecturer_name}' removed successfully!")
    except Exception as e:
        print(f"Error: Failed to remove lecturer. {e}")
