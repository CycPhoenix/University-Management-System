from registrar.register_new_students import register_new_students
from registrar.update_student_records import update_student_records
from registrar.manage_enrollments import manage_enrollments
from registrar.issue_transcripts import issue_transcripts
from registrar.view_student_information import view_student_information

def registrar_menu():
    """Main registrar menu to manage the university"""
    rm_art = r"""
     ___            _        _                   __ __                    
    | . \ ___  ___ <_> ___ _| |_ _ _  ___  _ _  |  \  \ ___ ._ _  _ _ 
    |   // ._>/ . || |<_-<  | | | '_><_> || '_> |     |/ ._>| ' || | |
    |_\_\\___.\_. ||_|/__/  |_| |_|  <___||_|   |_|_|_|\___.|_|_|`___|
              <___'                                                   """
    
    separator_length = max(len(line) for line in rm_art.splitlines())
    separator = "=" * separator_length

    while True:
        print()
        print(separator)
        print(rm_art)
        print(separator)
        print("--- Select a Category ---")
        print("1. Register New Student")
        print("2. Update Student Records")
        print("3. Manage Enrollments")
        print("4. Issue Transcripts")
        print("5. View Student Information")
        print("6. Back to Main Menu")

        choice = input("\nSelect an option: ")

        if choice == '1':
            register_new_students()
        elif choice == '2':
            update_student_records()
        elif choice == '3':
            manage_enrollments()
        elif choice == '4':
            student_id = input("Enter the Student ID to issue a transcript for: ").strip().upper()
            issue_transcripts(student_id)
        elif choice == '5':
            student_id = input("Enter the Student ID to view student information: ").strip().upper()
            view_student_information(student_id)
        elif choice == '6':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
