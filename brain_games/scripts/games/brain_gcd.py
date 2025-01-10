import math
import random

from brain_games.cli import welcome_user
from brain_games.engine import run_game


def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = math.gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, str(correct_answer)


def is_answer_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    run_game(name, generate_question, is_answer_correct)


if __name__ == '__main__':
    main()

