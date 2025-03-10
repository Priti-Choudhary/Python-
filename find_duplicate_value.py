def find_duplicates(arr):
    return [x for x in set(arr) if arr.count(x) > 1]

arr = [1, 2, 2, 3, 4, 4, 5]
print(find_duplicates(arr))