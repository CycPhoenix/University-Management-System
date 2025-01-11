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
    
    lecturer_data = []
    for lecturer in lecturers:
        lecturer_fields = lecturer.strip().split(',')
        if len (lecturer_fields) == 5:
            lecturer_data.append(lecturer_fields)
        else:
            lecturer_data.append(["[Corrupted Data]"])
    
    # Calculate column widths dynamically
    col_widths = [15, 25, 25, 30, 15]
    headers = ['ID', 'Name', 'Department', 'Email', 'Contact']

    # Add indentation
    indent = '   ' # Add 3 spaces of indentation

    header_row = "".join(f"{header:<{width}}" for header, width in zip(headers, col_widths))
    separator = "=" * len(header_row)

    print("--- Existing Lecturers ---")
    print(separator)
    print(indent + header_row)
    print(separator)

    for idx, lecturer_fields in enumerate(lecturer_data, start=1):
        if len(lecturer_fields) == 5:
            row = "".join(f"{field:<{width}}" for field, width in zip(lecturer_fields, col_widths))
            print(f"{idx:<3}{row}")
        else:
            print(f"{idx:<3}[Corrupted Data]")
    print(separator)

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

    selected_lecturer = lecturers[int(choice) - 1]
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
