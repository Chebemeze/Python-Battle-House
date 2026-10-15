def two_sum(nums, target):
    """ returns list of two numbers that are equal to target.
    Example of O(n^2)
    """
    res = []
    seen = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]== target and nums[i] not in seen and nums[j] not in seen:
                res.append((nums[i], nums[j]))
                seen.add(nums[i])
                seen.add(nums[j])
    return res
print(two_sum([2, 7, 11, 15, 5, 3], 9))


# def improved_two_sum(nums, target):
# """ This method returns the sum of the first two numbers that equals target.
# O(n) case.
# """
#     seen = {} #value -> index

#     for index in range(len(nums)):
#         remaining_num = target - nums[index]

#         if remaining_num in seen:
#             return [seen[remaining_num], index]

#         seen[nums[index]] = index
# print(improved_two_sum([2, 7, 11, 15, 5, 3], 9))


# def improved_two_sum(nums, target):
#     """ returns all unique sum of numbers.
#     O(n) case too.
#     """
#     seen = {}
#     all_combinations = []
#     repetition_checker = set()

#     for index in range(len(nums)):
#         remaining_num = target - nums[index]

#         if remaining_num in seen:
#             if remaining_num not in repetition_checker and nums[index] not in repetition_checker:
#                 all_combinations.append((remaining_num, nums[index]))
#                 repetition_checker.add(remaining_num)
#                 repetition_checker.add(nums[index])

#         seen[nums[index]] = index
#     return all_combinations
# print(improved_two_sum([2, 7, 11, 15, 5, 4, 7, 2, 4, 5], 9))
