def merge_intervals(intervals):
    # TODO: merge overlapping or touching intervals into consolidated ranges,
    # returned sorted by start value
    merged_interval = []
    sorted_interval = sorted(intervals)

    if len(sorted_interval) <= 1:
        return sorted_interval
    
    #handles list of tuples more than one (when there are more than one tuples inside the list)
    for index, interval in enumerate(sorted_interval):
        start_val = interval[0]
        end_val = interval[1]

        if index == 0:
            prev = (start_val, end_val)
            continue
        else:
            if start_val <= prev[1]:

                #this evealuates if the end_val is within the range of the previous tuple
                # or outside. If it is within the range, it means that both start_val and
                # end_val are both within the range of the previous tuple so
                # the previous tuple is maintained going forward but if end_val
                # is greater than the prev[1] value, it will be used instead - prev = (prev[0], end_val)
                if end_val < prev[1]:
                    end_val = prev[1]
                prev = (prev[0], end_val)
            elif start_val > prev[1]:
                merged_interval.append(prev)
                prev = (start_val, end_val)
    merged_interval.append(prev)
    return merged_interval

#test cases
print(merge_intervals([(8, 10), (1, 3), (2, 6)]))
print(merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]))
print(merge_intervals([(1, 3), (1, 3), (1,3), (1,3)]))
print(merge_intervals([]))
print(merge_intervals([(1, 4), (4, 5)]))