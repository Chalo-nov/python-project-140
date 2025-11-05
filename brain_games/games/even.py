import random

DESCRIPTION = 'Responde "yes" si el número es par, de lo contrario responde "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100

def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    is_even = (number % 2 == 0)
    
    question = str(number)
    
    if is_even:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    
    return question, correct_answer