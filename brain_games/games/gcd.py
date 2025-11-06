import random 

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_gcd(a,b):
    while b:
        a, b = b, a % b
    return a


def generate_round(): 
    # 1. Generar dos números aleatorios
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    # 2. Formular la pregunta
    question = f"{num1} {num2}"
    
    # 3. Calcular la respuesta correcta
    correct_answer = get_gcd(num1, num2)
    
    # 4. Devolver la pregunta y la respuesta (como cadena)
    return question, str(correct_answer)

