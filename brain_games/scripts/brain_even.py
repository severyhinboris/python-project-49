from random import randint


def brain_even():   
    print('Answer "yes" if the number is even, otherwise answer "no".')
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
            print(f"'{ans}' is wrong answer ;(. Correct answer was 
'{correct_ans}'.")
            print(f"Let's try again, {name}")
            correct_ans_row = 0
            break
        
