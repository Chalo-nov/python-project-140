import prompt
from brain_games.engine import run_game
from brain_games.games import even

def main():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!') 
    
    run_game(even.DESCRIPTION, even.generate_round) 
    
if __name__ == "__main__":
    main()