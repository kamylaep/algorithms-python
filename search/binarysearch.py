def binarysearch(search_element, elements=[]):
    if elements is None or len(elements) == 0:
        return -1

    low = 0
    high = len(elements) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = elements[middle]

        if guess == search_element:
            return middle
        elif guess > search_element:
            high = middle - 1
        else:
            low = middle + 1

    return -1
