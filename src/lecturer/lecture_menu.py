from lecturer.assign_modules import assign_modules
from lecturer.view_assigned_modules import view_assigned_modules
from lecturer.record_grades import record_grades
from lecturer.view_student_list import view_student_list
from lecturer.track_attendance import track_attendance
from lecturer.view_student_grades import view_student_grades

# Lecturer Menu
def lecturer_menu():
    while True:
        print("\nLecturer Menu:")
        print("1. Assign Modules")
        print("2. View Assigned Modules")
        print("3. Record Grades")
        print("4. View Student List")
        print("5. Track Attendance")
        print("6. View Student Grades")
        print("7. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            assign_modules()
        elif choice == '2':
            view_assigned_modules()
        elif choice == '3':
            record_grades()
        elif choice == '4':
            view_student_list()
        elif choice == '5':
            track_attendance()
        elif choice == '6':
            view_student_grades()
        elif choice == '7':
            print("Exiting Lecturer Menu.")
            break
        else:
            print("Invalid option. Please try again.")