import random

from brain_games.cli import welcome_user
from brain_games.engine import run_game


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), correct_answer


def is_answer_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    run_game(name, generate_question, is_answer_correct)


if __name__ == '__main__':
    main()
