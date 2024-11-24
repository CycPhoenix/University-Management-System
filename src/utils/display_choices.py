def display_choices(options):
    """Displays options to the user and return the selected index."""
    while True:
        # Display the options
        for idx, option in options.items():
            print(f"{idx}. {option}")

        # Prompt user for input
        choice = input("Select an option: ").strip()

        # Check if the input is valid
        if choice in options:
            return choice
        else:
            print("Invalid choice. Please try again.")
