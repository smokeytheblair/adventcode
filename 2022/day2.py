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


def count_score(input_file):
    games = load_inputs(input_file)

    my_points = 0
    for game in games:
        opponent, me = game.split()

        # rock
        if 'A' == opponent:
            # rock
            if 'X' == me:
                my_points += 1 + 3
            # paper
            elif 'Y' == me:
                my_points += 2 + 6
            # scissors
            elif 'Z':
                my_points += 3 + 0
        # paper
        elif 'B' == opponent:
            # rock
            if 'X' == me:
                my_points += 1 + 0
            # paper
            elif 'Y' == me:
                my_points += 2 + 3
            # scissors
            elif 'Z':
                my_points += 3 + 6
        # scissors
        elif 'C' == opponent:
            # rock
            if 'X' == me:
                my_points += 1 + 6
            # paper
            elif 'Y' == me:
                my_points += 2 + 0
            # scissors
            elif 'Z':
                my_points += 3 + 3

    print(f"Points = {my_points}")


def count_score_2(input_file):
    games = load_inputs(input_file)

    my_points = 0
    for game in games:
        opponent, me = game.split()

        # rock
        if 'A' == opponent:
            # lose
            if 'X' == me:
                # scissors
                my_points += 3 + 0
            # draw
            elif 'Y' == me:
                # rock
                my_points += 1 + 3
            # win
            elif 'Z':
                # paper
                my_points += 2 + 6
        # paper
        elif 'B' == opponent:
            # lose
            if 'X' == me:
                # rock
                my_points += 1 + 0
            # draw
            elif 'Y' == me:
                # paper
                my_points += 2 + 3
            # win
            elif 'Z':
                # scissors
                my_points += 3 + 6
        # scissors
        elif 'C' == opponent:
            # lose
            if 'X' == me:
                # paper
                my_points += 2 + 0
            # draw
            elif 'Y' == me:
                # scissors
                my_points += 3 + 3
            # win
            elif 'Z':
                # rock
                my_points += 1 + 6

    print(f"Points = {my_points}")


def main():
    parser = argparse.ArgumentParser(description="Count depth increases.")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if len(sys.argv) > 1:
        with args.file as input_file:
            if args.part == 1:
                count_score(input_file)
            elif args.part == 2:
                count_score_2(input_file)


if __name__ == "__main__":
    main()

