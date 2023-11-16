import random

def function_random_integer(min, max):
    """
    Generate a random integer between the specified minimum and maximum values.

    Parameters:
    - min (int): The minimum value for the random integer (inclusive).
    - max (int): The maximum value for the random integer (inclusive).

    Returns:
    int: A random integer between min and max.
    """
    return random.randint(min, max)

def function_random_operator():
    """
    Generate a random arithmetic operator.

    Returns:
    str: A random arithmetic operator chosen from the set {'+', '-', '*'}.
    """
    return random.choice(['+', '-', '*'])

def function_perform_operation(n1, n2, o):
    """
    Perform an arithmetic operation on two numbers.

    Parameters:
    - n1 (int): The first operand.
    - n2 (int): The second operand.
    - o (str): The arithmetic operator ('+', '-', '*').

    Returns:
    tuple: A tuple containing a string representation of the operation (e.g., "2 + 3") and the result of the operation.
    """
    operation_str = f"{n1} {o} {n2}"

    if o == '+':
        result = n1 + n2
    elif o == '-':
        result = n1 - n2
    else:
        result = n1 * n2

    return operation_str, result

def math_quiz():
    s = 0
    total_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random numbers and operator
        n1 = function_random_integer(1, 10)
        n2 = function_random_integer(1, 20)
        o = function_random_operator()

        # Get the correct answer and display the question
        PROBLEM, ANSWER = function_perform_operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")

        # Get user's answer with input validation
        while True:
            useranswer = input("Your answer: ")
            try:
                useranswer = int(useranswer)
                break  # Break out of the loop if conversion to int is successful
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Check correctness
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
