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
            print("'Answer Checker' selected!")
            print("-"*20 + "HOW TO USE ANSWER CHECKER" + "-"*20)
            print("\nUse this function to build and solve a math problem.")
            print("You'll enter the first digit, what operation to use (add, subtract, divide, or multiply), and what you think the answer will be.")
            print("The answer checker will then check if the answer to your problem was correct.")
            print("You'll have three attempts to get it right, then the correct answer will be revealed!\n")

            num1 = input("Enter the first number: ")
            
            num2 = input("Enter the second number: ")

            operator = input("placeholder")
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