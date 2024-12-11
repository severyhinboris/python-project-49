#!/usr/bin/env python3

from random import randint
from brain_games.cli import welcome_user


def brain_even(name):
    correct_ans_row = 0
    while correct_ans_row < 3:
        num = randint(1, 1000)
        print('Question:', num)
        ans = input('Your answer: ')
        if num % 2 == 0:
            correct_ans = 'yes'
        else:
            correct_ans = 'no'
        if ans == correct_ans:
            print('Correct!')
            correct_ans_row += 1
            if correct_ans_row == 3:
                print(f"Congratulations, {name}")
        else:
            print(f"""'{ans}' is wrong answer ;(.
Correct answer was '{correct_ans}'.""")
            print(f"Let's try again, {name}")
            correct_ans_row = 0
            break


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    brain_even(name)


if __name__ == "__main__":
    main()
