
def recursive(nth):
    if nth <= 1:
        return nth
    return recursive(nth-1) + recursive(nth-2)


def dynamic(nth):
    if nth <= 1:
      return nth

    fib_seq = [0] * (nth + 2)
    fib_seq[0] = 0
    fib_seq[1] = 1

    for i in range(2, nth + 1):
        fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2]

    return fib_seq[nth]


def lasttwo(nth):
    if nth <= 1:
      return nth

    fibonacci = 0
    first_value = 0
    second_value = 1

    for i in range (2, nth + 1):
      fibonacci = first_value + second_value
      first_value = second_value
      second_value = fibonacci

    return fibonacci;
