#! /home/vkhalaim/hexlet/bin/python

from brain_games.cli import start_game
import brain_games.games.progression as progression


def main():
    start_game(progression)


if __name__ == '__main__':
    main()
