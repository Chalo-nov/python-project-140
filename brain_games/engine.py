import prompt

ROUNDS_COUNT = 3

def run_game(description, generate_round):
    """
    Motor genérico que orquesta la bienvenida, las rondas y la validación.
    
    :param description: Reglas del juego (string).
    :param generate_round: Función que devuelve la pregunta y la respuesta correcta.
    """
    print('Welcome to the Brain Games!')
    print(description)
    print()
    
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print()

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_round()
        
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        
        if user_answer.lower() == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return 

    print(f'Congratulations, {user_name}!')