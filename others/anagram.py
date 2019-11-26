from sort.bubblesort import bubblesort

def isanagram(a='', b=''):
    if a is None or b is None:
        return False

    striped_a = a.replace(' ', '').lower()
    striped_b = b.replace(' ', '').lower()

    if len(striped_a) != len(striped_b):
        return False

    sorted_a = bubblesort(list(striped_a))
    sorted_b = bubblesort(list(striped_b))

    return sorted_a == sorted_b
