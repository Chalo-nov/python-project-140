import random

DESCRIPTION = "What is the result of the expression?


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    

def generate_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    
    question = f"{num1} {operator} {num2}"
    correct_answer_value = calculate(num1, num2, operator)
    
    return question, str(correct_answer_value)