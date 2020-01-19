import prompt

ROUNDS = 3


def get_user_name(greeting=None):
    print('Welcome to the Brain Games!')

    if greeting:
        print(greeting + '\n')

    name = prompt.string('May I have your name? ')
    print('Hello, {0}!\n'.format(name))
    return name


def start_game(game):
    game_greeting = game.GAME_RULE
    name = get_user_name(game_greeting)

    for i in range(0, ROUNDS):
        question, correct_answer = game.round()
        print('Question: ', question)
        answer = prompt.string("Your answer: ")

        if answer != correct_answer:
            print('{0} is wrong answer ;(. Correct answer was {1}.\n \
            Let\'s try again, {2}!'.format(answer, correct_answer, name))
            return

        print('Correct!')

    print('Congratulations, {0}!'.format(name))
