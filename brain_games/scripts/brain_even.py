import random

from brain_games.cli import welcome_user


def brain_even(name):
    correct_answers = 0
    while correct_answers < 3:
        question = random.randint(1, 100)
        print(f'Question: {question}')
        correct_answer = 'yes' if question % 2 == 0 else 'no'
        user_answer = input('Your answer: ')        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f" '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            correct_answers += 1
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    brain_even(name)


if __name__ == '__main__':
    main()

