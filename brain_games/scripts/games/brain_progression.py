import random

from brain_games.engine import run_game
from brain_games.cli import welcome_user


def generate_question():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = [start + step * i for i in range(length)]
    missing_index = random.randint(0, length - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)


def is_answer_correct(user_answer, correct_answer):
    return user_answer == correct_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What number is missing in the progression?')
    run_game(name, generate_question, is_answer_correct)


if __name__ == '__main__':
    main()

