def remove_element(arr, target):
    return [x for x in arr if x != target]

arr = [1, 2, 3, 4, 5]
print(remove_element(arr, 3))