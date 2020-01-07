import prompt
from brain_games.games.cli import run
from random import randint


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = run()
    start(name)


def incorrect(name, answer):
    if answer == 'yes':
        correct = 'no'
    else:
        correct = 'yes'

    print('{0} is wrong answer ;(. Correct answer was {1}.\n \
        Let\'s try again, {2}!'.format(answer, correct, name))


def start(name):
    for i in range(3):
        number = randint(0, 100)
        print('Question: {0}'.format(number))
        answer = prompt.string("Your answer: ")
        if answer in ('yes', 'no'):
            if (answer == 'yes' and number % 2 == 0) or \
               (answer == 'no' and number % 2 != 0):
                print("Correct!")
                if (i == 2):
                    print('Congratulations, {0}!'.format(name))
                continue
            else:
                incorrect(name, answer)
                break
        else:
            incorrect(name, answer)
            break
