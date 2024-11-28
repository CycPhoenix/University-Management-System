from admin.admin_menu import admin_menu

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
        print()
        print("1. Administrator")
        print("2. Lecturer")
        print("3. Student")
        print("4. Registrar")
        print("5. Accountant")
        print("6. Exit System")

        choice = input("Select an option: ")

        if choice == '1':
            admin_menu()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
