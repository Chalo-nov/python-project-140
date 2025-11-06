from brain_games.engine import run_game
from brain_games.games import calc

def main():
    # 1. Diálogo de bienvenida y obtención del nombre
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print() # Para espaciado
    
    run_game(calc.DESCRIPTION, calc.generate_round) 
    
if __name__ == "__main__":
    main()