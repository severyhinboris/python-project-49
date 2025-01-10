import random

from brain_games.cli import welcome_user
from brain_games.engine import run_game


def generate_question():
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)    
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return f"{num1} {operator} {num2}", str(correct_answer)


def is_answer_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    run_game(name, generate_question, is_answer_correct)


if __name__ == '__main__':
    main()

