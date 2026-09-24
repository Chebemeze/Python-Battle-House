def find_index(numbers, target):
    # TODO: locate `target` in the sorted list `numbers` and return its index,
    # or -1 if it isn't there
    a = -1
    decision_list = [index for index, value in enumerate(numbers) if value == target]
    if decision_list:
        a = decision_list[0]
    return a
print(find_index([], 5))
print(find_index([1,2,3,4,5,6,7], 8))