from admin.admin_menu import admin_menu
from utils.display_choices import display_choices

def main_menu():
    """Main menu to select system role."""
    while True:
        print("\n--- University Management System ---")
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
        
        print(ascii_art)

        options = {
            '1': 'Administrator',
            '2': 'Lecturer',
            '3': 'Student',
            '4': 'Registrar',
            '5': 'Accountant',
            '6': 'Exit System'
        }
        choice = display_choices(options)

        if choice == '1':
            admin_menu()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
