from admin.admin_menu import admin_menu
from lecturer.lecture_menu import lecturer_menu
from student.student_menu import student_menu
from accountant.accountant_menu import accountant_menu
from registrar.registrar_menu import registrar_menu

def main_menu():
    """Main menu to select system role."""
    while True:
        ascii_art = r"""
                  _____                    _____                    _____              
                 /\    \                  /\    \                  /\    \         
                /::\____\                /::\____\                /::\    \        
               /:::/    /               /::::|   |               /::::\    \       
              /:::/    /               /:::::|   |              /::::::\    \      
             /:::/    /               /::::::|   |             /:::/\:::\    \     
            /:::/    /               /:::/|::|   |            /:::/__\:::\    \    
           /:::/    /               /:::/ |::|   |            \:::\   \:::\    \   
          /:::/    /      _____    /:::/  |::|___|______    ___\:::\   \:::\    \  
         /:::/____/      /\    \  /:::/   |::::::::\    \  /\   \:::\   \:::\    \ 
        |:::|    /      /::\____\/:::/    |:::::::::\____\/::\   \:::\   \:::\____\
        |:::|____\     /:::/    /\::/    / ~~~~~/:::/    /\:::\   \:::\   \::/    /
         \:::\    \   /:::/    /  \/____/      /:::/    /  \:::\   \:::\   \/____/ 
          \:::\    \ /:::/    /               /:::/    /    \:::\   \:::\    \     
           \:::\    /:::/    /               /:::/    /      \:::\   \:::\____\    
            \:::\__/:::/    /               /:::/    /        \:::\  /:::/    /    
             \::::::::/    /               /:::/    /          \:::\/:::/    /     
              \::::::/    /               /:::/    /            \::::::/    /      
               \::::/    /               /:::/    /              \::::/    /       
                \::/____/                \::/    /                \::/    /        
                 ~~                       \/____/                  \/____/         
        """
        separator_length = max(len(line) for line in ascii_art.splitlines())
        separator = "=" * separator_length
        
        print(separator)
        print(ascii_art)
        print(separator)
        print("--- Select a Category ---")
        print("1. Administrator")
        print("2. Lecturer")
        print("3. Student")
        print("4. Registrar")
        print("5. Accountant")
        print("6. Exit System")

        choice = input("\nSelect an option: ")

        if choice == '1':
            admin_menu()
        elif choice == '2':
            lecturer_menu()
        elif choice == '3':
            student_menu()
        elif choice == '4':
            registrar_menu()
        elif choice == '5':
            accountant_menu()
        elif choice == '6':
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
