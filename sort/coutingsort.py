def countingsort(arr=[]):
    if arr is None or len(arr) == 0:
        return arr

    counts = [0] * (max(arr) + 1)

    for x in arr:
        counts[x] += 1

    curr = 0

    for x in range(len(counts)):
        for y in range(counts[x]):
            arr[curr] = x
            curr += 1

    return arr
