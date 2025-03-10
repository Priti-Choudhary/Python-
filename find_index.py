def find_index(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1

arr = [1, 2, 3, 4, 5]
print(find_index(arr, 3))