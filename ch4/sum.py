def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([1,2,3,4]))

def rec_sum(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    else:
        return rec_sum(arr[0:1]) + rec_sum(arr[1:len(arr)])

print(rec_sum([1,2,3,4]))
