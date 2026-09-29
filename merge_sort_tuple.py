"A modified merge sort for a list of tuple where each tuple is shaped
like (lower, higher)"

def merge_Sort(un_sorted):
    if len(un_sorted) <= 1:
        return un_sorted
    
    middle = len(un_sorted)//2
    left = merge_Sort(un_sorted[:middle])
    right = merge_Sort(un_sorted[middle:])

    return merge(left, right)

def merge(left, right):
    res = []
    i = j= 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

print(merge_Sort([(8,10),(3,19),(1,20),(20,40)]))
    
