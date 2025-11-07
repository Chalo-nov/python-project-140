import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number < 2:
        return False
    # Solo necesitamos verificar divisores hasta la raíz cuadrada del número
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def generate_round():
    # 1. Generar un número aleatorio
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    
    # 2. Formular la pregunta
    question = str(number)
    
    # 3. Calcular la respuesta correcta ("yes" o "no")
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    
    # 4. Devolver la pregunta y la respuesta
    return question, correct_answer