from random import randint, choice
from operator import sub, add, mul

MAX_NUMBER = 100
GAME_RULE = 'What is the result of the expression?'
operators = {'+': add, '-': sub, '*': mul}


def round():
    number1 = randint(0, MAX_NUMBER)
    number2 = randint(0, MAX_NUMBER)
    operator = choice('+-*')

    question = str(number1) + operator + str(number2)
    correct_answer = str(operators[operator](number1, number2))

    return question, correct_answer
