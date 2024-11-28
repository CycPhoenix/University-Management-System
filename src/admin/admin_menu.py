from admin.courses.manage_courses import manage_courses
from admin.students.manage_students import manage_students
from admin.lecturers.manage_lecturers import manage_lecturers
from admin.reports.generate_reports import generate_reports
from admin.view_all_data import view_all_data
from utils.display_choices import display_choices

def admin_menu():
    """Main admin menu to manage the university system."""
    am_art = r"""
     ___    _         _        __ __                
    | . | _| |._ _ _ <_>._ _  |  \  \ ___ ._ _  _ _     
    |   |/ . || ' ' || || ' | |     |/ ._>| ' || | |
    |_|_|\___||_|_|_||_||_|_| |_|_|_|\___.|_|_|`___|
    """

    separator_length = max(len(line) for line in am_art.splitlines())
    separator = "=" * separator_length

    while True:
        print()
        print(separator)
        print(am_art)
        print(separator)
        options = {
            '1': 'Manage Courses',
            '2': 'Manage Students',
            '3': 'Manage Lecturers',
            '4': 'Generate Reports',
            '5': 'View All Data',
            '6': 'Back to Main Menu'
        }
        choice = display_choices(options)

        if choice == '1':
            manage_courses()
        elif choice == '2':
            manage_students()
        elif choice == '3':
            manage_lecturers()
        elif choice == '4':
            generate_reports()
        elif choice == '5':
            view_all_data()
        elif choice == '6':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
