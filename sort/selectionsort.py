def selectionsort(arr=[]):
    if arr is None or len(arr) == 0:
        return arr

    sorted_arr = []

    for _ in range(len(arr)):
        smallest = min(arr)
        sorted_arr.append(smallest)
        arr.remove(smallest)

    return sorted_arr
