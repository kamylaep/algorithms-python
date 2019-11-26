def insertionsort(arr=[]):
    if arr is None or len(arr) == 0:
        return arr

    for x in range(len(arr)):
        curr = arr[x]
        y = x - 1

        while y >= 0 and arr[y] > curr:
            arr[y + 1] = arr[y]
            y -= 1

        arr[y + 1] = curr

    return arr
