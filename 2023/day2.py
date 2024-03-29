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
    game_id = int(game_report[5:game_report.index(':')])

    draws = game_report[game_report.index(':')+1:].split(';')
    print(draws)

    for draw in draws:
        print(draw)

        cubes_by_color = draw.strip().split(',')
        for color in cubes_by_color:
            color_count = color.strip().split(' ')
            print(color_count)

            if int(color_count[0].strip()) > loaded_cubes[color_count[1]]:
                return False, game_id

    return True, game_id


def part1(input_file):
    inputs = load_inputs(input_file)

    loaded_cubes = {'red': 12, 'green': 13, 'blue': 14}

    possible_draws_sum = 0
    for game_report in inputs:
        game = parse_game(game_report, loaded_cubes)

        if game[0]:
            possible_draws_sum += game[1]

    print(f'Possible draws sum: {possible_draws_sum}')


def parse_game2(game_report:str):
    game_id = int(game_report[5:game_report.index(':')])

    draws = game_report[game_report.index(':')+1:].split(';')
    print(draws)

    min_cubes = {'red': 0, 'green': 0, 'blue': 0}

    for draw in draws:
        print(draw)

        cubes_by_color = draw.strip().split(',')
        for color in cubes_by_color:
            color_count = color.strip().split(' ')
            print(color_count)

            current_count = int(color_count[0].strip())
            if current_count > min_cubes[color_count[1]]:
                min_cubes[color_count[1]] = int(color_count[0].strip())

    return game_id, min_cubes


def part2(input_file):
    inputs = load_inputs(input_file)

    sum_of_mins = 0
    for game_report in inputs:
        game = parse_game2(game_report)
        sum_of_mins += game[1]['red'] * game[1]['green'] * game[1]['blue']

    print(f'Sum of mins: {sum_of_mins}')


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

