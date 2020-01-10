#!/usr/bin/env python3

from brain_games.cli import start_game
import brain_games.games.gcd as gcd


def main():
    start_game(gcd)


if __name__ == '__main__':
    main()
