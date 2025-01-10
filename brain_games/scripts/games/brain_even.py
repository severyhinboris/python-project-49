import random

from brain_games.cli import welcome_user

from brain_games.engine import run_game


def generate_question():
    question = random.randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), correct_answer


def is_answer_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    run_game(name, generate_question, is_answer_correct)


if __name__ == '__main__':
    main()

