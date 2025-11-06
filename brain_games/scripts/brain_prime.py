from brain_games.engine import run_game
from brain_games.games import prime


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print()
    
    run_game(prime.DESCRIPTION, prime.generate_round) 

  
if __name__ == "__main__":
    main()