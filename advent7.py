import sys


def print_usage(name):
    print("python3 {} <input_file>".format(name))
    print("-1 - compute the first part of the problem.")
    print("-2 - compute the second part of the problem.")

def get_top_keys(prereqs):
    top_keys = [k for k in prereqs]

    for key in prereqs:
        for value in prereqs.values():
            if key in value and key in top_keys:
                top_keys.remove(key)

    return sorted(top_keys)


def load_inputs(input_file):
    print("loading inputs...")

    prereqs = {}

    for line in input_file:
        parts = line.split(" ")
        step = parts[1]
        prereqs.setdefault(step, [])
        prereq = parts[7]
        prereqs[step].append(prereq)

    print("prereqs:\n{}".format(prereqs))
    return prereqs


def are_prereqs_met(key, prereqs, step_order):
    met = False

    my_prereqs = [id for id, vals in prereqs.items() if key in vals]
    my_prereqs_met = [False for req in my_prereqs if req not in step_order]
   
    if False not in my_prereqs_met and key not in step_order:
        met = True

    # print("are_prereqs_met=={}, key:{}, my_prereqs:{}, step_order:{}".format(met, key, "".join(my_prereqs), "".join(step_order)))
    return met


def find_next_keys(prereqs, all_keys, step_order):
    next_keys = []

    for key in all_keys:
        if are_prereqs_met(key, prereqs, step_order):
            next_keys.append(key)

    # print("next_keys: {}".format(next_keys))
    return sorted(next_keys)

def process_prereqs(input_file):
    print("processing prerequisite sequence...")

    prereqs = load_inputs(input_file)

    all_keys = get_top_keys(prereqs)
    for req in prereqs.values():
        all_keys = all_keys + req
    print("all_keys:\n{}".format(all_keys))

    # for prereq, children in prereqs.items():
    #     print("{} is prerequsite of {}".format(prereq, children))
    # print(get_top_keys(prereqs))

    step_order = ""
    while len(step_order) < len(all_keys):
        next_keys = find_next_keys(prereqs, all_keys, step_order)
        if 0 < len(next_keys):
            step_order += next_keys[0]
            all_keys.remove(next_keys[0])
            # print("step_order: {}\nall_keys: {}".format(step_order, all_keys))
        else:
            break

    print("step_order: {}".format(step_order))

def main():
    if len(sys.argv) > 2:
        input_file = open(sys.argv[2], 'r')
        if "-1" in sys.argv[1]:
            process_prereqs(input_file)
        elif "-2" in sys.argv[2]:
            process_part2(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()
