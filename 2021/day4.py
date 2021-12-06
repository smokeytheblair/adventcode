import sys
import argparse

bingo_balls = None
bingo_cards = None

def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def load_inputs(input_file):
    global bingo_balls
    global bingo_cards

    lines = list(input_file)

    bingo_balls = lines[0].replace("\n", "").split(",")
    print(bingo_balls)

    card = []
    next_card = False
    for line in lines:
        line = line.replace("\n", "")
        if -1 < line.find(","):
            continue
        if line == "":
            if 0 != len(card):
                print(card)
                bingo_cards.append(card)
            card = list()
        else:
            row = line.split(" ")
            print(row)
            if 0 == len(card):
                for num in row:
                    card.append(list(num))
            else:
                index = 0
                for num in row:
                    card[index].append(num)
                    index += 1


    print(cards)
    # for line in report:

    return report

def play_bingo(input_file):
    directions = load_inputs(input_file)
#    print(f"{directions}")

    num_bits = len(directions[0])
    count_0 = 0
    count_1 = 0
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(num_bits):
        count_0 = 0
        count_1 = 0
 #       print(f"i: {i}")
        for direction in directions:
  #          print(f"direction[{i}] = {direction[i]}")
            if direction[i] == "0":
                count_0 += 1
            else:
                count_1 += 1

#        print(f"count_0:{count_0}, count_1:{count_1}")

        if count_0 > count_1:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"


    gamma_int = int(gamma_rate, 2)
    epsilon_int = int(epsilon_rate, 2)

    print(f"gamma rate:{gamma_int} * epsilon rate:{epsilon_int} = {gamma_int*epsilon_int}")

def filter_o2_numbers(codes, i):
#    print(f"filter o2 i: {i}, codes: {codes}")

    if len(codes) <= 1:
        return codes

    if i >= len(codes[0]):
        return codes

    count_0 = 0
    count_1 = 0
    o2_nums = []

    for code in codes:
        if code[i] == "0":
            count_0 += 1
        else:
            count_1 += 1

    for code in codes:
        if count_1 >= count_0 and code[i] == "1":
            o2_nums.append(code)
        elif count_0 > count_1 and code[i] == "0":
            o2_nums.append(code)

    return filter_o2_numbers(o2_nums, i+1)


def filter_co2_numbers(codes, i):
#    print(f"filter co2 i: {i}, codes: {codes}")
    if len(codes) <= 1:
        return codes

    if i >= len(codes[0]):
        return codes

    count_0 = 0
    count_1 = 0
    co2_nums = []

    for code in codes:
        if code[i] == "0":
            count_0 += 1
        else:
            count_1 += 1

#    print(f"count_0 = {count_0}, count_1 = {count_1}")
    for code in codes:
        if count_0 <= count_1 and code[i] == "0":
            co2_nums.append(code)
        elif count_1 < count_0 and code[i] == "1":
            co2_nums.append(code)

    return filter_co2_numbers(co2_nums, i+1)

def compute_o2_2(input_file):
    codes = load_inputs(input_file)

    num_bits = len(codes[0]) - 1
    count_0 = 0
    count_1 = 0
    o2_nums = []
    co2_nums = []
    i = 0
    #       print(f"i: {i}")
    for code in codes:
        #          print(f"direction[{i}] = {direction[i]}")
        if code[i] == "0":
            count_0 += 1
        else:
            count_1 += 1

    for code in codes:
        if count_0 > count_1 and code[i] == "0":
            o2_nums.append(code)
        elif count_1 >= count_0 and code[i] == "1":
            o2_nums.append(code)

    for code in codes:
        if count_0 <= count_1 and code[i] == "0":
            co2_nums.append(code)
        elif count_1 < count_0 and code[i] == "1":
            co2_nums.append(code)

    o2_nums = filter_o2_numbers(o2_nums, 1)
    co2_nums = filter_co2_numbers(co2_nums, 1)

    print(f"o2 {o2_nums}, co2 {co2_nums}")

    o2_setting = int(o2_nums[0],2)
    co2_setting = int(co2_nums[0],2)

    print(f"o2 * co2 = {o2_setting*co2_setting}")

def main():
    parser = argparse.ArgumentParser(description="Bingo")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                play_bingo(input_file)
            elif args.part == 2:
                compute_o2_2(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()

