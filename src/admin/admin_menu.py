# admin_menu.py
from .courses.manage_courses import manage_courses
from .students.manage_students import manage_students
from .lecturers.manage_lecturers import manage_lecturers
from .reports.generate_reports import generate_reports
from .data.view_all_data import view_all_data

def admin_menu():
    while True:
        print("\n--- Administrator Menu ---")
        print("1. Manage Courses")
        print("2. Add/Remove Student")
        print("3. Manage Lecturers")
        print("4. Generate Reports")
        print("5. View All Data")
        print("6. Back to Main Menu")
        print("--------------------------")
        choice = input("\nSelect an option: ").strip()

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
            print("\nReturning to main menu...")
            break
        else:
            print("Invalid option. Please try again.")