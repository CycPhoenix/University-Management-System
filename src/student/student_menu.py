from admin.courses.view_all_courses import view_all_courses
from student.modules.view_attendence import access_attendance_record
from student.modules.view_grade import view_grades
from student.modules.enroll_module import enroll_module
from student.modules.unenroll_module import unenroll_module

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
            student_id = input("Enter your student ID: ").lower()
            access_attendance_record(student_id)
        elif choice == '2':
            student_id = input("Enter your student ID: ").lower()
            view_grades(student_id)
        elif choice == '3':
            view_all_courses()
        elif choice == '4':
                inputs = input("Enter your student ID and module code to enroll (e.g., TP085702 CS101): ").split()
                if len(inputs) != 2:
                 print("Invalid input. Please provide both your student ID and module code.")
                else:
                    student_id, module_code = inputs
                    enroll_module(student_id, module_code)
        elif choice == '5':
            inputs = input("Enter your student ID and module code to unenroll (e.g., tp085702 CS101): ").split()
            if len(inputs) != 2:
                print("Invalid input. Please provide both your student ID and module code.")
            else:
                student_id, module_code = inputs
                unenroll_module(student_id, module_code)
        elif choice == '6':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
