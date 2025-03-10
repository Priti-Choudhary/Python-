def insert_element(arr, target, pos):
    return arr[:pos] + [target] + arr[pos:]

arr = [1, 2, 3, 4, 5]
print(insert_element(arr, 10, 2))