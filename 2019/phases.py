def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

for a in range(5,10):
    for b in range(5,10):
        for c in range(5,10):
            for d in range(5,10):
                for e in range(5,10):
                    perms = [a, b, c, d, e]
                    perms = unique(perms)

                    if len(perms) == 5:
                        print(f'{perms[0]},{perms[1]},{perms[2]},{perms[3]},{perms[4]}')
