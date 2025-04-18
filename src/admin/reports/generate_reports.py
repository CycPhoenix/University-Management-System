from admin.reports.total_overview import total_overview
from admin.reports.students_and_lecturers_by_department import students_and_lecturers_by_department
from admin.reports.total_courses_by_type import total_courses_by_type

def generate_reports():
    """Menu to generate reports."""
    gr_art = r"""
     ___                             _         ___                       _          
    /  _>  ___ ._ _  ___  _ _  ___ _| |_ ___  | . \ ___  ___  ___  _ _ _| |_ ___
    | <_/\/ ._>| ' |/ ._>| '_><_> | | | / ._> |   // ._>| . \/ . \| '_> | | <_-<
    `____/\___.|_|_|\___.|_|  <___| |_| \___. |_\_\\___.|  _/\___/|_|   |_| /__/
                                                        |_|                     
    """
    
    # Calculate the length based on the line in the ASCII art
    separator_length = max(len(line) for line in gr_art.splitlines())
    separator = "=" * separator_length

    while True:
        print()
        print(separator)
        print(gr_art)
        print(separator)
        print("1. Total Overview")
        print("2. Studentes and Lecturers by Department")
        print("3. Total Courses by Type")
        print("4. Back to Admin Menu")

        choice = input("Select an option: ")

        if choice == '1':
            total_overview()
        elif choice == '2':
            students_and_lecturers_by_department()
        elif choice == '3':
            total_courses_by_type()
        elif choice == '4':
            print("Returning to admin menu...")
            break
        else:
            print("Invalid choice. Please try again.")
