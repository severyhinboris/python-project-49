def run_game(name, generate_question, is_answer_correct):
    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = generate_question()
        print(f'Question: {question}')        
        user_answer = input('Your answer: ')        
        if is_answer_correct(user_answer, correct_answer):
            print('Correct!')
            correct_answers += 1
            if correct_answers == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

