def second_largest(arr):
    if len(set(arr)) < 2:
        return None
    return sorted(set(arr))[-2]

arr = [1, 2, 3, 4, 5]
print(second_largest(arr))