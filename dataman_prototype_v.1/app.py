# Elijah Dixon
# 11/9/2026
# CTS-285

import logic as fn

ANS_CHECKER_OPT = ['1','2']


def menu():
    '''
    Displays the menu options.
    '''
    print("""
1) Answer Checker
2) Memory Bank (Work in Progress)
3) Number Guesser (Work in Progress)
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
            print("-"*20 + " HOW TO USE ANSWER CHECKER " + "-"*20)

            print("\nUse this function to build and solve a math problem.")
            # I opted for building the problem piece by piece, as this made it easier to put into the logic function.
            print("You'll enter the first digit, what operation to use (add, subtract, divide, or multiply), and what you think the answer will be.")
            print("The answer checker will then check if the answer to your problem was correct.")
            print("You'll have three attempts to get it right, then the correct answer will be revealed!\n")

            ans_check_sentinel = '1'

            while ans_check_sentinel !=  '2':
                num1 = input("\nEnter the first number: ").strip()

                # Input validation.
                while not num1.isdigit():
                    print("Please enter a valid number.")
                    num1 = input("\nEnter the first number: ").strip()


                operation = input("\nAdd (+), Subtract(-), Multiply(*), or Divide(/): ").strip()

                # Input validation.
                while operation not in fn.MATH_SYMBOLS:
                    print("Please enter a valid operator.")
                    operation = input("\nAdd (+), Subtract(-), Multiply(*), or Divide(/): ").strip()
                
                num2 = input("\nEnter the second number: ")

                # Input validation.
                while not num2.isdigit():
                    print("Please enter a valid number.")
                    num2 = input("\nEnter the second number: ").strip()

                while num2 == '0' and operation == "/":
                    # This message would need to be changed as to not confuse students when they use the actusl appliaction.
                    # I just couldn't think of a consise and correct way to explain this right now.
                    print(f"\nPlease select a number other than {num2} to divide {num1} by.")
                    num2 = input("Enter the second number: ").strip()

                # Initialize or re-initialize the attempts for this specific problem.
                # I wanted to initialize this inside of the logic, but I wasnt sure how I wanted to implement it.
                # I decided to store the attempts here, but keep the logic behind them in the logic file.
                attempts = fn.ANSWER_CHECKER_ATTEMPTS

                print(f"\nYour math problem: {num1} {operation} {num2} = ?")

                # Counts the attempts that the user has and displays it.
                answer = input(f"Enter your answer ({attempts} attempts left.): ")
                # Calculate once, and skips 
                correct, true_ans = fn.calculate_answer(num1, operation, num2, answer)

                # Clearly and unmistakably tell the user their answer is correct.
                if correct == True:
                    print()
                    print("-"*20 + " !!! CORRECT !!! " + "-"*20)

                # This loop handles the attempts. The structure could be much better, though.
                while attempts > 0 and correct == False:

                    correct, attempts = fn.count_attempts(correct, attempts)

                    # I thought about putting this part in the logic layer, but since its just display
                    # and not any actual calculations, I kept it here.
                    print()

                    # Clearly and unmistakably tell the user their answer is incorrect.
                    print("*"*20 + " INCORRECT " + "*"*20)

                    if attempts <= 0:
                        print(f"\nOut of attempts...")
                        print(f"Here is the solution: {num1} {operation} {num2} = {true_ans} ")

                    else:
                        print(f"\nYour math problem: {num1} {operation} {num2} = ?")
                        answer = input(f"Try again! ({attempts} attempts left.): ")

                        correct, true_ans = fn.calculate_answer(num1, operation, num2, answer)

                # Asks if you want to run answer checker again without going to menu.
                # The web version wouldnt require you to do this, as answer checker would be the default function.
                print("""\nWould you like to enter another problem?
                1) Yes
                2) Exit to main menu.
                """)

                # Just validates the answer to prevent issues if something wrong is inputted.
                # Not really needed as this frontend will be changed very soon...
                ans_check_sentinel = input("Enter a choice: ")
                while ans_check_sentinel not in ANS_CHECKER_OPT:
                    ans_check_sentinel = input("Please enter a valid choice: ")


        elif choice == '2':
            # Will call the python function that runs the 'Memory Bank' function.
            print("\n'Memory Bank' selected!")
            print("This function is still a work in progress. Please choose another.")
            

        elif choice == '3':
            # Will call the python function that runs the 'Number Guesser" function.
            print("\n'Number Guesser' selected!")
            print("This function is still a work in progress. Please choose another.")
            

    
    



if __name__ == '__main__':
    main()
    input("\nProgram Terminated... Press ENTER to close.")