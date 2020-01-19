from random import randint

GAME_RULE = 'What number is missing in the progression?'
MAX_START = 100
ELEMENTS = 10
MAX_STEP = 10


def round():
    missed_element_index = randint(0, ELEMENTS - 1)
    step_progression = randint(0, MAX_STEP)
    start_progression = randint(0, MAX_START)
    question = ""
    element = start_progression
    missed_element = 0

    for i in range(0, ELEMENTS):
        element += step_progression
        if i == missed_element_index:
            missed_element = element
            question += '..'
        else:
            question += str(element)
        question += ' '
    return question, str(missed_element)
