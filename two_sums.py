def two_sums(nums, target):
    nums_check = set()
    target_sum = []
    for i,j in nums:
        if i+j == target and i not in nums_check and j not in nums_check:
            target_sum.append((i,j))
            nums_check.add(i)
            nums_check.add(j)
    return target_sum

nums = [(2,3),(3,2),(0,5),(1,2),(5,0)]
print(two_sums(nums, 5))