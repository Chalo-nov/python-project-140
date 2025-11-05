from brain_games.games import progression
from brain_games.engine import run_game 



def main():
    run_game(progression.DESCRIPTION, progression.generate_round)


if __name__ == "__main__":
    main()