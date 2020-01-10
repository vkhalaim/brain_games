from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUM = 100


def isPrime(n):
    if n <= 3:
        return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5

    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6

    return True


def round():
    number = randint(1, MAX_NUM)

    if isPrime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = str(number)

    return question, correct_answer
