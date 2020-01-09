#! /home/vkhalaim/hexlet/bin/python

from brain_games.cli import start_game
import brain_games.games.even as even


def main():
    start_game(even)


if __name__ == '__main__':
    main()
