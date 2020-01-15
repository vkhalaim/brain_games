from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'
MAX_NUM = 100


def gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2

    return n1


def round():
    num1 = randint(0, MAX_NUM)
    num2 = randint(0, MAX_NUM)

    correct_answer = str(gcd(num1, num2))
    question = str(num1) + ' ' + str(num2)

    return question, correct_answer
