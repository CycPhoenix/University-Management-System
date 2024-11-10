from functions import admin_functions, lecturer_functions, student_functions, registrar_functions, accountant_functions

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
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            admin_functions.admin_menu()
        elif choice == '4':
            registrar_functions.registrar_menu()
        elif choice == '6':
            print("\nExiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main_menu()