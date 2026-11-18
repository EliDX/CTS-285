This file contains information regarding the usage of AI for this project.

# How much code was written by ai?
- ## No generative AI has been used to write code for the assignment as of 11/17/2026, though I did use two prompts to get assistance in finding out how I could build the attempt system.

- ## The prompts are as follows:

    - "Give me an example of how I could possibly implement an attempt system for the answer checker menu option, whose logic stays inside of logic.py. Do not write any code in the files themselves."

    - ### This prompt was submitted to VS codes built-in Copiolot Fusion which chose GPT-6 Luna to complete my request. The full response is below, though I did not directly use any of the information below.


    -"In `app.py`, the menu currently asks for one answer and calls `calculate_answer`. In `logic.py`, `calculate_answer` returns `True` for a correct answer but implicitly returns `None` for a wrong one. You could move the attempt loop into `logic.py` and have the menu call one function instead.

    For example, add a result helper and an attempt-runner in `logic.py`:

    ```python
    def _get_result(num1, operator, num2):
        num1 = int(num1)
        num2 = int(num2)

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            return num1 // num2

        raise ValueError("Unsupported operator.")


    def calculate_answer(num1, operator, num2, user_answer):
        return int(user_answer) == _get_result(num1, operator, num2)


    def run_answer_checker(num1, operator, num2, max_attempts=3):
        if max_attempts <= 0:
            raise ValueError("max_attempts must be greater than zero.")

        correct_answer = _get_result(num1, operator, num2)
        attempts_used = 0

        while attempts_used < max_attempts:
            remaining = max_attempts - attempts_used
            guess = input(f"Enter your answer ({remaining} attempts remaining): ").strip()

            try:
                guess = int(guess)
            except ValueError:
                print("Please enter a whole number. This won't count as an attempt.")
                continue

            attempts_used += 1

            if calculate_answer(num1, operator, num2, guess):
                print("Correct!")
                return True

            print("Incorrect.")

        print(f"Out of attempts. The correct answer was {correct_answer}.")
        return False
    ```

    Then, in `app.py`, keep displaying the math problem but replace the answer prompt and `calculate_answer` call with:

    ```python
    fn.run_answer_checker(num1, operation, num2)
    ```

    This example counts only valid whole-number guesses as attempts and preserves the current integer-division behavior. It also explicitly rejects division by zero. No files were changed."

    - ### This was followed up by the following prompt:
    
    - "Is it possible to keep all print statements in the app.py file, and only logic in the logic.py file? The frontend (app.py) may be changed to a different format, and print atements directly from the logic may cause issues. (If possible, do this without classes/objects.)" 

    - ### This was the response:

    "Yes. A simple way to keep **all `print()` and `input()` calls in `app.py`** is to pass two functions from the frontend into `logic.py`: one to collect a guess, and one to display feedback. `logic.py` can still own the attempt counter and answer checking, without using classes.

    Assuming `logic.py` has a helper such as `_get_result(...)` to calculate the correct answer, its attempt function could look like this:

    ```python
    def run_answer_checker(num1, operator, num2, get_guess, show_feedback,
                        max_attempts=3):
        if max_attempts <= 0:
            raise ValueError("max_attempts must be greater than zero.")

        correct_answer = _get_result(num1, operator, num2)

        for attempt in range(1, max_attempts + 1):
            guess = get_guess(attempt, max_attempts)

            if guess == correct_answer:
                show_feedback("correct", attempt, correct_answer)
                return True

            if attempt == max_attempts:
                show_feedback("out_of_attempts", attempt, correct_answer)
            else:
                show_feedback("incorrect", attempt, None)

        return False
    ```

    In `app.py`, define the callbacks so all user interaction stays there:

    ```python
    def get_guess(attempt, max_attempts):
        while True:
            raw = input(f"Attempt {attempt} of {max_attempts}: ").strip()
            try:
                return int(raw)
            except ValueError:
                print("Please enter a whole number.")


    def show_feedback(status, attempt, correct_answer):
        if status == "correct":
            print("Correct!")
        elif status == "incorrect":
            print("Incorrect. Try again.")
        else:
            print(f"Out of attempts. The correct answer was {correct_answer}.")
    ```

    Then call the checker from the menu code:

    ```python
    fn.run_answer_checker(
        num1, operation, num2, get_guess, show_feedback
    )
    ```

    The logic module decides whether each guess is correct and how many attempts remain; the app supplies the input and output behavior. That also makes it easier to replace the console frontend later—the callbacks could use a GUI instead. I haven’t changed any files."

    - ### I did not use any of the code that the AI generated directly (eg. copy & paste), but the second prompt in particular helped me understand how I could built the attempt system.

