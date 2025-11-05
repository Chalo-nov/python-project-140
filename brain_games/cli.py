from brain_games.cli import welcome_user # <--- ¡Importación Absoluta!

def welcome_user():

    print('¡Bienvenido(a) a los Juegos Mentales!')
    
    name = prompt.string('¿Cuál es tu nombre? ')
    
    print(f'Hola, {name}!')