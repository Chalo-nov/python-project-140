import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    
    name = prompt.string('¿Cuál es tu nombre? ')

    print(f'Hola, {name}!')