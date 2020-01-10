#!/usr/bin/env python3

from brain_games.cli import start_game
import brain_games.games.prime as prime


def main():
    start_game(prime)


if __name__ == '__main__':
    main()
