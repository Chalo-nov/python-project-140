from brain_games.games import gcd
from brain_games.engine import run_game 



def main():
    run_game(gcd.DESCRIPTION, gcd.generate_round)


if __name__ == "__main__":
    main()
    