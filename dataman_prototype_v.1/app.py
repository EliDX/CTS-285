# Elijah Dixon
# 11/9/2026
# CTS-285

import logic as fn


def menu():
    '''
    Displays the menu options.
    '''
    print("""
1) Answer Checker
2) Memory Bank (Work in Progress)
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

            
            num1 = input("Enter the first number: ").strip()

            while not num1.isdigit():
                print("Please enter a valid number.")
                num1 = input("Enter the first number: ").strip()


            operation = input("Add (+), Subtract(-), Multiply(*), or Divide(/): ").strip()

            while operation not in fn.MATH_SYMBOLS:
                print("Please enter a valid operator.")
                operation = input("Add (+), Subtract(-), Multiply(*), or Divide(/): ").strip()
            
            num2 = input("Enter the second number: ")

            while not num2.isdigit():
                print("Please enter a valid number.")
                num2 = input("Enter the second number: ").strip()

            

            # I though about putting this part in the logic layer, but since its just display
            # and not any actual calculations, I kept it here.
            print(f"\nYour math problem: {num1} {operation} {num2} = ?")
            answer = input("Enter your answer: ")

            # Program calculates answer a

            
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