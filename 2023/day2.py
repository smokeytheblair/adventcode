import sys
import argparse

reset_report = None


def load_inputs(input_file):
    global reset_report
    report = []

    if reset_report is not None:
        report = reset_report.copy()
    else:
        report = list(input_file)

        if reset_report is None:
            reset_report = report.copy()

    return report


def parse_game(game_report:str, loaded_cubes):
    game_id = game_report[5:game_report.index(':')]

    draws = game_report[game_report.index(':')+1:].split(';')

    for draw in draws:
        print(draw)


def part1(input_file):
    inputs = load_inputs(input_file)

    possible_games = []
    loaded_cubes = {'red': 12, 'green': 13, 'blue': 14}

    for game_report in inputs:
        game = parse_game(game_report, loaded_cubes)


def part2(input_file):
    inputs = load_inputs(input_file)


def main():
    parser = argparse.ArgumentParser(description="Advent of Code.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                part1(input_file)
            elif args.part == 2:
                part2(input_file)


if __name__ == "__main__":
    main()

