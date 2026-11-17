# The file containing individual functions to be used in the dataman project.

# Symbols allowed to be inputted for math problems in answer checker.
MATH_SYMBOLS = ['+', '-', '*', '/']

def calculate_answer(num1, operator, num2, user_answer):
    '''
    Calculate the answer to a math problem created by the user.
    Used in the Answer Checker function.
    '''
    num1 = int(num1)
    num2 = int(num2)
    user_answer = int(user_answer)
    # What operator is chosen changes the calculation.
    if operator == "+":
        true_ans = num1 + num2

    elif operator == "-":
        true_ans = num1 - num2

    elif operator == "*":
        true_ans = num1 * num2
        
    # Choosing division would have calculated a remainder, though I haven't found a way to display this properly along with the answer.    
    elif operator == "/":
        true_ans = num1 // num2
        #remainder = num1 % num2

    if user_answer == true_ans:
        return True
    