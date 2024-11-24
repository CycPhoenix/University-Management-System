# from src import lecturer_functions, student_functions, registrar_functions, accountant_functions
from admin.admin_menu import admin_menu


def main_menu():
    while True:
        print("\n--- University Management System ---")
        print("1. Administrator")
        print("2. Lecturer")
        print("3. Student")
        print("4. Registrar")
        print("5. Accountant")
        print("6. Exit")
        print("------------------------------------")
        choice = input("\nSelect an option: ").strip()
        
        if choice == '1':
            admin_menu()
        elif choice == '6':
            print("\nExiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main_menu()