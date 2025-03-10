def common_values(arr1, arr2):
    return [x for x in set(arr1) & set(arr2)]

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print(common_values(arr1, arr2))