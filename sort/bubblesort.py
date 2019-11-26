def bubblesort(arr=[]):
    if arr is None or len(arr) == 0:
        return arr

    arr_length = len(arr)

    for i in range(arr_length):
        something_sorted = False

        for j in range(0, arr_length - 1 - i):
            if arr[j] < arr[j + 1]:
                continue

            something_sorted = True
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not something_sorted:
            break

    return arr
