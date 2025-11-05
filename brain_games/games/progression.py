import random

DESCRIPTION = '¿Qué número falta en la progresión?'
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10
MIN_LENGTH = 5
MAX_LENGTH = 10

def generate_progression(start, step, length):
    progression = []
    current = start
    for _ in range(length):
        progression.append(str(current))
        current += step
    return progression

def generate_round():
    # 1. Generar parámetros aleatorios
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    
    # 2. Crear la progresión y seleccionar el índice oculto
    progression_list = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    
    # 3. Guardar la respuesta correcta
    correct_answer = progression_list[hidden_index]
    
    # 4. Ocultar el número y formar la pregunta
    progression_list[hidden_index] = '..'
    question = ' '.join(progression_list)
    
    return question, correct_answer