import os

# This function safely gets an integer input form the user.
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# This function clears the terminal screen.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pauses execution until the user presses Enter.
def pause():
    input("\nPress Enter to continue...")