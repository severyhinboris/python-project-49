import random

from brain_games.cli import welcome_user


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

    return f'Question: {num1} {operator} {num2}', str(correct_answer)


def brain_calc(name):
    correct_ans_row = 0
    while correct_ans_row < 3:
        question, correct_answer = generate_question()
        print(question)
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            correct_ans_row += 1
            if correct_ans_row == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('What is the result of the expression?')
    brain_calc(name)


if __name__ == '__main__':
    main()

