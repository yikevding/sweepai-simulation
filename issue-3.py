def is_strictly_increasing(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i-1]:
            return False
    return True