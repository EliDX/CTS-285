# Elijah Dixon
# 11/9/2026
# CTS-285

def menu():
    '''
    Displays the menu options.
    '''
    print("""
1) Answer Checker
2) Memory Bank
3) Number Guesser
------------------------------
0) Exit Program
    """)

def main():
    # Data man ASCII art. Just for fun!
    print("""
██████╗  █████╗ ████████╗ █████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗ ████║██╔══██╗████╗  ██║
██║  ██║███████║   ██║   ███████║██╔████╔██║███████║██╔██╗ ██║
██║  ██║██╔══██║   ██║   ██╔══██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██████╔╝██║  ██║   ██║   ██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝""")
    print('='*62)

    # Sentinel variable for while loop.
    choice = 'default'

    # Main program loop.
    while choice != '0':
        menu()
        choice = input("Enter a choice: ")

        if choice == '1':
            # Will call the pyhton function that runs the 'Answer Checker' function.
            print("\nTesting... Testing... Choice chosen!!!!")
            pass

        elif choice == '2':
            # Will call the python function that runs the 'Memory Bank' function.
            print("\nTesting... Testing... Choice chosen???")
            pass

        elif choice == '3':
            # Will call the python function that runs the 'Number Guesser" function.
            print("\nTesting... Testing... Choice chosen...")
            pass

    
    



if __name__ == '__main__':
    main()
    input("\nProgram Terminated... Press ENTER to close.")