from math import trunc

def count(text, looking_for, size):
    return (text.count(looking_for) * (size // len(text))) + text[:size % len(text)].count(looking_for)
