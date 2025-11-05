# Importa la función que ejecuta el juego (el motor)
from brain_games.engine import run_game 
# Importa la logica del juego
from brain_games.games import calc

def main():
    """Punto de entrada: Llama al motor de juego con la lógica de 'calc'."""
    run_game(calc.DESCRIPTION, calc.generate_round)

if __name__ == "__main__":
    main()