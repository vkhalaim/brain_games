from random import randint, choice
from operator import sub, add, mul

MAX_NUMBER = 100
GAME_RULE = 'What is the result of the expression?'
OPERATORS = [('+', add), ('-', sub), ('*', mul)]


def round():
    number1 = randint(0, MAX_NUMBER)
    number2 = randint(0, MAX_NUMBER)
    operator, operation = choice(OPERATORS)

    question = '{0} {1} {2}'.format(number1, operator, number2)
    correct_answer = str(operation(number1, number2))

    return question, correct_answer
