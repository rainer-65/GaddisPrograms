def maximum(values):
    maximum = values[0]

    for val in values:
        if val > maximum:
            maximum = val

    return maximum


def minimum(values):
    minimum = values[0]

    for val in values:
        if val < minimum:
            minimum = val

    return minimum


def total(values):
    total = 0
    for i in values:
        total += i
    return total


def is_empty(values):
    if len(values):
        return False
    else:
        return True
