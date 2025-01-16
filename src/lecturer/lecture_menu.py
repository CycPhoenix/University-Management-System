from lecturer.view_assigned_modules import view_assigned_modules
from lecturer.record_grades import record_grades
from lecturer.view_student_list import view_student_list
from lecturer.track_attendance import track_attendance
from lecturer.view_student_grades import view_student_grades

# Lecturer Menu
def lecturer_menu():
    while True:
        print("\nLecturer Menu:")
        print("1. View Assigned Modules")
        print("2. Record Grades")
        print("3. View Student List")
        print("4. Track Attendance")
        print("5. View Student Grades")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            view_assigned_modules()
        elif choice == '2':
            record_grades()
        elif choice == '3':
            view_student_list()
        elif choice == '4':
            track_attendance()
        elif choice == '5':
            view_student_grades()
        elif choice == '6':
            print("Exiting Lecturer Menu.")
            break
        else:
            print("Invalid option. Please try again.")