# TO-DO: complete the help function below to merge 2 sorted arrays
import math


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    c = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr[c] = arrA[a]
            a = a + 1
            c = c + 1
        else:
            merged_arr[c] = arrB[b]
            b = b + 1
            c = c + 1

    while a < len(arrA):
        merged_arr[c] = arrA[a]
        c = c + 1
        a = a + 1
    while b < len(arrB):
        merged_arr[c] = arrB[b]
        c = c + 1
        b = b + 1
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    rounded_mean = math.ceil(len(arr) / 2)
    x = [0] * rounded_mean
    y = []

    for i in range(0, len(arr)):
        if (i < rounded_mean):
            x[i] = arr[i]
        else:
            y.append(arr[i])

    x = merge_sort(x)
    y = merge_sort(y)
    arr = merge(x, y)

    return arr


test_arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(test_arr))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
