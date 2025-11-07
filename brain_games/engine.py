import prompt

ROUNDS_COUNT = 3


def run_game(user_name, description, generate_round):
    print(description)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_round()
        
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer.lower() == correct_answer:
            print('Correct!')
        else:
            
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            return 

    print(f'Congratulations, {user_name}!')