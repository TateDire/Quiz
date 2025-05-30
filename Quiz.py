import random

# To check if the user enters a valid response
def string_checker(question, viable_ans=None):
    if viable_ans is None:
        viable_ans = ["yes", "no"]

    error = f"Please enter a valid option from: {viable_ans}"

    while True:
        user_response = input(question).lower()

        for item in viable_ans:
            if item == user_response or user_response == item[0]:
                return item

        print(error)
        print()

# The instructions
def instructions():
    print("""

--- How to Play ---

First, choose how many rounds you want to do.
Or, just press <enter> for endless mode.

You’ll be asked one random maths question each round.
Try to get as many right as you can. Good luck!

""")

# Ask how many rounds to play
def int_check(question):
    while True:
        error = "Please enter a whole number 1 or more."

        to_check = input(question)

        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)
            if response < 1:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

# Create a random question
def generate_question():
    math_type = random.choice(['+', '-', '*', '/'])

    if math_type == '+':
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        question1 = f"What is {a} + {b}? "
        answer = a + b

    elif math_type == '-':
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        a, b = max(a, b), min(a, b)  # Makes sure the answer isn't negative
        question1 = f"What is {a} - {b}? "
        answer = a - b

    elif math_type == '*':
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        question1 = f"What is {a} x {b}? "
        answer = a * b

    else:  # Division with a whole number result
        b = random.randint(1, 12)
        answer = random.randint(1, 12)
        a = b * answer  # Makes sure division works evenly
        question1 = f"What is {a} ÷ {b}? (Whole number only) "

    return question1, answer

# Setup
mode = "regular"
rounds_played = 0
rounds_correct = 0
rounds_incorrect = 0
quiz_history = []

# Main routine
print("\n✖️➕➖➗ Math Quiz ➗➖➕✖️\n")

want_instructions = string_checker("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

num_rounds = int_check("How many rounds would you like to play? Press <enter> for infinite: ")

if num_rounds == "infinite":
    print("Infinite mode selected!")
    mode = "infinite"
    num_rounds = 5

# Game loop
while rounds_played < num_rounds:

    print(f"\n--- Round {rounds_played + 1} ---")

    # Ask a random maths question
    question, answer = generate_question()

    try:
        user_answer = int(input(question))

        if user_answer == answer:
            print("Correct! ✅")
            rounds_correct += 1
            feedback = "Correct"
        else:
            print(f"Incorrect! ❌ The right answer was {answer}")
            rounds_incorrect += 1
            feedback = "Incorrect"

    except ValueError:
        print(f"Incorrect ❌ The right answer was {answer}")
        rounds_incorrect += 1
        feedback = "Incorrect"

    rounds_played += 1
    quiz_history.append(f"Round {rounds_played}: {feedback}")

    if mode == "infinite":
        num_rounds += 1

# Show results
if rounds_played > 0:
    print("\n--- Quiz Summary ---")
    print(f"Total Correct ✅: {rounds_correct}")
    print(f"Total Incorrect ❌: {rounds_incorrect}")

    see_history = string_checker("Would you like to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

    print("\nThanks for playing!")

else:
    print("🐔🐔🐔 Oops - You chickened out! 🐔🐔🐔")
