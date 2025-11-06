import prompt
from brain_games.engine import run_game
from brain_games.games import prime

def main():
    # 1. Diálogo de bienvenida y obtención del nombre (AQUÍ ES DONDE DEBE ESTAR)
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print() 
    
    # 2. Llamada al motor con TRES argumentos
    run_game(user_name, prime.DESCRIPTION, prime.generate_round) 
    
if __name__ == "__main__":
    main()