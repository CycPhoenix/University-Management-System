from admin.courses.manage_courses import manage_courses
from admin.students.manage_students import manage_students
from admin.lecturers.manage_lecturers import manage_lecturers
from admin.reports.generate_reports import generate_reports
from admin.view_all_data import view_all_data

from admin.courses.view_all_courses import view_all_courses
from student.modules.view_attendence import access_attendance_record

def student_menu():
    """Main student menu to manage the university system."""
    am_art = r"""
     ___    _          _             _     __ __                    
    / __> _| |_ _ _  _| | ___ ._ _ _| |_  |  \  \ ___ ._ _  _ _ 
    \__ \  | | | | |/ . |/ ._>| ' | | |   |     |/ ._>| ' || | |
    <___/  |_| `___|\___|\___.|_|_| |_|   |_|_|_|\___.|_|_|`___|
                                                            
    """

    separator_length = max(len(line) for line in am_art.splitlines())
    separator = "=" * separator_length

    while True:
        print()
        print(separator)
        print(am_art)
        print(separator)
        print("1. View Attedence Record")
        print("2. View Grade")
        print("3. View Module")
        print("4. Enroll Module")
        print("5. Unenroll Module")
        print("6. Back to Main Menu")

        choice = input("\nSelect an option: ")

        if choice == '1':
            student_id = input("Enter your student ID: ")
            access_attendance_record(student_id)
        elif choice == '2':
            view_grades(student_id)
        elif choice == '3':
            view_all_courses()
        elif choice == '4':
            module_code = input("Enter module code to enroll: ")
            enroll_in_module(student_id, module_code)
        elif choice == '5':
            module_code = input("Enter module code to unenroll: ")
            unenroll_from_module(student_id, module_code)
        elif choice == '6':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
