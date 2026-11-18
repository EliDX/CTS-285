# The file containing individual functions to be used in the dataman project.

# Symbols allowed to be inputted for math problems in answer checker.
MATH_SYMBOLS = ['+', '-', '*', '/']
ANSWER_CHECKER_ATTEMPTS = 3

def calculate_answer(num1, operator, num2, user_answer):
    '''
    Calculate the answer to a math problem created by the user.
    Used in the Answer Checker function.

    May need to be adjusted to work with the memory back function in the future.'
    Most likely will need to be combined with the 'count_attempts' function.

    '''

    # The function itself converts everything into integers.
    # This (should) create less issues with the frontend in the future.
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
        
    # Choosing division would have also calculated a remainder, though I haven't found a way to display this properly along with the answer.    
    elif operator == "/":
        true_ans = num1 // num2
        #remainder = num1 % num2

    if user_answer == true_ans:
        return True, true_ans

    else:
        return False, true_ans

def count_attempts(result, attempts):
    '''
    This function only exists to count the attempts that the user has left. Could be implemented into the 
    'calculate_answer' function, but I havent figured out how to approach this yet.
    '''

    if result == True:
        return True, attempts

    elif result == False:
        attempts =  attempts - 1
        return False, attempts

    
    