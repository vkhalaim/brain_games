#!/usr/bin/env python3

from brain_games.cli import start_game
import brain_games.games.calc as calc


def main():
    start_game(calc)


if __name__ == '__main__':
    main()
