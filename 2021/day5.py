import sys
import argparse



def print_usage(name, input_file):
    print(f"Usage: python3 {name} {input_file}")

def load_inputs(input_file):
    lines = list(input_file)

    vectors = []
    for line in lines:
        line = line.replace("\n", "")
        coords = line.split(" -> ")
        start_coords = coords[0].split(",")
        end_coords = coords[1].split(",")
        vectors.append((start_coords, end_coords))

    return vectors

def count_overlaps(vectors):
    count = 0
    already_checked = {}
    for vector_1 in vectors:
        for vector_2 in vectors:
            if vector_1 is vector_2:
                continue

            if True == already_checked.get(str(vector_1)+str(vector_2)):
                continue

            if True == already_checked.get(str(vector_2)+str(vector_1)):
                continue

            #keep the lines going left to right
            if int(vector_1[0][1]) == int(vector_1[1][1]) and int(vector_1[1][0]) < int(vector_1[0][0]):
                x_0 = int(vector_1[1][0])
                y_0 = int(vector_1[1][1])
                x_1 = int(vector_1[0][0])
                y_1 = int(vector_1[0][1])
                #print(f"swapped {vector_1}: p0 [{x_0},{y_0}] and p1 [{x_1},{y_1}] to keep line left to right")
            elif int(vector_1[1][0]) == int(vector_1[0][0]) and int(vector_1[0][1]) > int(vector_1[1][1]):
                x_0 = int(vector_1[1][0])
                y_0 = int(vector_1[1][1])
                x_1 = int(vector_1[0][0])
                y_1 = int(vector_1[0][1])
                #print(f"swapped {vector_1}: p0 [{x_0},{y_0}] and p1 [{x_1},{y_1}] to keep line top down")
            else:
                x_0 = int(vector_1[0][0])
                y_0 = int(vector_1[0][1])
                x_1 = int(vector_1[1][0])
                y_1 = int(vector_1[1][1])

            #skip diagonal lines
            x_s_1 = x_1 - x_0
            y_s_1 = y_1 - y_0
            if 0 != x_s_1 and 0 != y_s_1:
                # print(f"Slope of x1: {x_1} - {x_0} = {x_s_1}")
                # print(f"Slope of y1: {y_1} - {y_0} = {y_s_1}")
                continue

            #keep the lines going left to right
            if int(vector_2[1][0]) < int(vector_2[0][0]):
                x_2 = int(vector_2[1][0])
                y_2 = int(vector_2[1][1])
                x_3 = int(vector_2[0][0])
                y_3 = int(vector_2[0][1])
                #print(f"swapped {vector_2}: p2 [{x_2},{y_2}] and p3 [{x_3},{y_3}] to keep line left to right")
            elif int(vector_2[1][0]) == int(vector_2[0][0]) and int(vector_2[0][1]) > int(vector_2[1][1]):
                x_0 = int(vector_2[1][0])
                y_0 = int(vector_2[1][1])
                x_1 = int(vector_2[0][0])
                y_1 = int(vector_2[0][1])
                #print(f"swapped {vector_2}: p2 [{x_2},{y_2}] and p3 [{x_3},{y_3}] to keep line top down")
            else:
                x_2 = int(vector_2[0][0])
                y_2 = int(vector_2[0][1])
                x_3 = int(vector_2[1][0])
                y_3 = int(vector_2[1][1])

            #skip diagonal lines
            x_s_2 = x_3 - x_2
            y_s_2 = y_3 - y_2
            if 0 != x_s_2 and 0 != y_s_2:
                # print(f"Slope of x2: {x_3} - {x_2} = {x_s_2}")
                # print(f"Slope of y2: {y_3} - {y_2} = {y_s_2}")
                continue

            #make left most vector the first vector
            if (x_2 < x_0 and y_0 == y_2) or (x_0 == x_2 and y_2 < y_0):
                temp_x = x_0
                x_0 = x_2
                x_2 = temp_x
                temp_y = y_0
                y_0 = y_2
                y_2 = temp_y

                temp_x = x_1
                x_1 = x_3
                x_3 = temp_x
                temp_y = y_1
                y_1 = y_3
                y_3 = temp_y

                # print(f"swapped vector_1:{vector_1} with vector_2:{vector_2} as \n*** p0[{x_0},{y_0}], p1[{x_1},{y_1}], p2[{x_2},{y_2}], p3[{x_3},{y_3}]")

            # print(f"comparing vector_1:{vector_1} to vector_2:{vector_2} as \n*** p0[{x_0},{y_0}], p1[{x_1},{y_1}], p2[{x_2},{y_2}], p3[{x_3},{y_3}]")

            if y_0 == y_1 == y_2 == y_3:
                if x_1 > x_2:
                    count_delta = x_1 - x_2
                    if x_3 < x_1:
                        count_delta -= x_1 - x_3
                        count_delta += 1

                    print(f"*** p0[{x_0},{y_0}], p1[{x_1},{y_1}], p2[{x_2},{y_2}], p3[{x_3},{y_3}]")
                    print(f"vector_1: {vector_1} intersects with vector_2: {vector_2} : {count_delta} (parallel)")
                    count += count_delta
                elif x_1 == x_2:
                    # print(f"vector_1: {vector_1} intersects with vector_2: {vector_2} : 1 (parallel)")
                    count += 1
            elif x_0 == x_1 == x_2 == x_3:
                if y_1 > y_2:
                    count_delta = y_1 - y_2
                    if y_3 < y_1:
                        count_delta -= y_1 - y_3
                        count_delta += 1

                    print(f"*** p0[{x_0},{y_0}], p1[{x_1},{y_1}], p2[{x_2},{y_2}], p3[{x_3},{y_3}]")
                    print(f"vector_1: {vector_1} intersects with vector_2: {vector_2} : {count_delta} (parallel)")
                    count += count_delta
                elif y_1 < y_2:
                    count_delta = y_2 - y_1
                    if y_3 > y_1:
                        count_delta -= y_1
                    # print(f"vector_1: {vector_1} intersects with vector_2: {vector_2} : {count_delta} (parallel)")
                    count += count_delta
                elif y_1 == y_2:
                    # print(f"vector_1: {vector_1} intersects with vector_2: {vector_2} : 1 (parallel)")
                    count += 1
            elif y_0 == y_1 and x_0 <= x_2 and x_3 <= x_1 and y_0 >= y_2 and y_1 <= y_3:
                # print(f"vector_1: {vector_1} intersects with vector_2: {vector_2} : 1")
                count += 1
            elif x_0 == x_1 and x_0 <= x_2 and x_3 >= x_1 and y_0 <= y_2 and y_1 >= y_3:
                # print(f"vector_1: {vector_1} intersects with vector_2: {vector_2} : 1")
                count += 1

            already_checked[str(vector_1)+str(vector_2)] = True

    return count

def find_overlaps(input_file):
    vectors = load_inputs(input_file)
    print(vectors)

    count = count_overlaps(vectors)

    print(f"Count overlaps: {count}")

def main():
    parser = argparse.ArgumentParser(description="Vents")
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument('--part', type=int, required=True, help='Part 1 or Part 2')

    args = parser.parse_args()

    if (len(sys.argv) > 1):
        with args.file as input_file:
            if args.part == 1:
                find_overlaps(input_file)
            elif args.part == 2:
                find_overlaps(input_file)
    else:
        print_usage(sys.argv[0], args.file)

if __name__ == "__main__":
    main()

