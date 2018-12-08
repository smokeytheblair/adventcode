import sys
from datetime import datetime
import re


def print_usage(name):
    print("python3 {} <input_file>".format(name))

def find_most_asleep(notes):
    print("finding most asleep time...")

    sleeping_minutes = {}
    sleepiest_guard = {}
    guard_id = 0
    asleep_time = 0
    wake_time = 0
    
    for time in sorted(notes):
        # print("{} {}".format(time, notes[time]))
        if notes[time].startswith("Guard"):
            guard_id = re.findall("\d+", notes[time])[0]
        elif "asleep" in notes[time]:
            asleep_time = int(time.minute) 
        elif "wakes" in notes[time]:
            wake_time = int(time.minute) 

            sleepiest_guard.setdefault(guard_id,0)
            sleepiest_guard[guard_id] += wake_time - asleep_time

            for minute in range(wake_time - asleep_time):
                key = "{}:{}".format(guard_id, asleep_time+minute)
                sleeping_minutes.setdefault(key, 0)
                sleeping_minutes[key] += 1
                # print("{} => {}".format(key, sleeping_minutes[key]))
            wake_time = 0
            asleep_time = 0

    most_minutes = int(max(sleepiest_guard.values()))
    sleepiest_id = [k for k, v in sleepiest_guard.items() if v == most_minutes]

    max_keys = dict([(k,sleeping_minutes[k]) for k, v in sleeping_minutes.items() if sleepiest_id[0] in k])
    # print(max_keys)

    max_minutes = int(max(max_keys.values()))
    # print(max_minutes) 
    
    target_key = [k for k, v in max_keys.items() if v == max_minutes]
    print(target_key)

    guard_id = re.findall("\d+", target_key[0])[0]
    sleepiest_minute = re.findall("\d+", target_key[0])[1]
    print(int(sleepiest_minute) * int(guard_id))
    
    max_minute = int(max(sleeping_minutes.values()))
    most_asleep_key = [k for k, v in sleeping_minutes.items() if v == max_minute]
    guard_id = re.findall("\d+", most_asleep_key[0])[0]
    sleepiest_minute = re.findall("\d+", most_asleep_key[0])[1]
    print(most_asleep_key)
    print(int(sleepiest_minute) * int(guard_id))

        

def sort_notes(input_file, notes):
    # [1518-05-01 23:46] Guard #2503 begins shift
    for note in input_file:
        timestamp = datetime.strptime(note[1:17], "%Y-%m-%d %H:%M")
        msg = note[19:]

        notes[timestamp] = msg


def find_tired_guard(input_file):
    print("finding tired guard...")

    notes = {}
    sort_notes(input_file, notes)

    find_most_asleep(notes)


def main():
    if len(sys.argv) > 1:
        input_file = open(sys.argv[1], 'r')
        find_tired_guard(input_file)
        input_file.close()
    else:
        print_usage(sys.argv[0])

if __name__ == "__main__":
    main()
