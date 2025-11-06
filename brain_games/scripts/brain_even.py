import prompt
from brain_games.engine import run_game
from brain_games.games import even

def main():
    # El diálogo de bienvenida va aquí para que el tester lo pueda ejecutar
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print() 
    
    run_game(user_name, even.DESCRIPTION, even.generate_round) 
    
if __name__ == "__main__":
    main()