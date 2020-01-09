from random import randint

GAME_RULE = 'Answer "yes" if number even otherwise answer "no".'
MAX_NUM = 100


def round():
    number = randint(0, MAX_NUM)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return number, correct_answer
