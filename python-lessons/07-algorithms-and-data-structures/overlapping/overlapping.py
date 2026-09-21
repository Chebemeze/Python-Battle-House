def merge_intervals(intervals):
    # TODO: merge overlapping or touching intervals into consolidated ranges,
    # returned sorted by start value
    new_list = []

    for index, val in enumerate(intervals):
        index+=1
        start_val = val[0]
        end_val = val[1]

        already_exist = (start_val, end_val) in new_list

        if index != 1:
            base_list = [i for i in range(start_val, end_val+1)]
            continue
        else:
            if start_val in base_list and end_val in base_list:
                if not already_exist:
                    new_list.append((base_list[0],base_list[-1]))
            elif start_val in base_list and end_val not in base_list:
                if not already_exist:
                    new_list.append((base_list[0], end_val))
            else:
                if not already_exist:
                    new_list.append((base_list[0],base_list[-1]))
                    new_list.append((start_val, end_val))
    return new_list

print(merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]))
print(merge_intervals([(1, 3), (1, 3), (1,3), (1,3)]))