from utils.load_data import load_data
from settings import LECTURERS_FILE

def view_all_lecturers():
    """View all lecturers in the system."""
    val_art = r"""
     _ _  _               ___  _  _   _               _                             
    | | |<_> ___  _ _ _  | . || || | | |   ___  ___ _| |_ _ _  _ _  ___  _ _  ___
    | ' || |/ ._>| | | | |   || || | | |_ / ._>/ | ' | | | | || '_>/ ._>| '_><_-<
    |__/ |_|\___.|__/_/  |_|_||_||_| |___|\___.\_|_. |_| `___||_|  \___.|_|  /__/
    """

    # Load lecturers data
    try:
        lecturers = load_data(LECTURERS_FILE)
        if not lecturers:
            print("No lecturers found.")
            return
    except FileNotFoundError:
        print(f"Error: File '{LECTURERS_FILE}' not found.")
        return

    # Parse lecturers into fields
    lecturer_data = []
    for lecturer in lecturers:
        lecturer_fields = lecturer.strip().split(',')
        if len(lecturer_fields) == 5:
            lecturer_data.append(lecturer_fields)
        else:
            lecturer_data.append(["[Corrupted Data]"])

    # Calculate column widths dynamically
    col_widths = [15, 25, 25, 30, 15] # Adjust widths as needed
    headers = ["ID", "Name", "Department", "Email", "Contact"]

    # Add indentation
    indent = "   " # Add 3 spaces of indentation

    # Print header
    header_row = "".join(f"{header:<{width}}" for header, width in zip(headers, col_widths))
    separator = "=" * len(header_row)
    print()
    print(separator)
    print(val_art)
    print(separator)
    print(indent + header_row)
    print(separator)

    # Print lecturer details
    for idx, lecturer_fields in enumerate(lecturer_data, start=1):
        if len(lecturer_fields) == 5:
            row = "".join(f"{field:<{width}}" for field, width in zip(lecturer_fields, col_widths))
            print(f"{idx:<3}{row}")
        else:
            print(f"{idx:<3}[Corrupted Data]")

    print(separator)
