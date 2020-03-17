arr = [6, 3, 9, 1, 3, 7, 2]
print('before', arr)


def selection_sort(arr):
    ranger = len(arr) - 1
    for i in range(0, ranger):
        discovered_floor = i
        for j in range(i, ranger + 1):
            if arr[j] < arr[discovered_floor]:
                discovered_floor = j

        temp_index = arr[i]
        arr[i] = arr[discovered_floor]
        arr[discovered_floor] = temp_index

    return arr


print('after', selection_sort(arr))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    ranger = len(arr) - 1
    for i in range(0, ranger):
        for j in range(0, ranger - i):
            if arr[j] > arr[j + 1]:
                temp_index = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp_index
    return arr


print("BUBBLE SORT", bubble_sort(arr))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr


print("COUNT SORT", count_sort(arr))
