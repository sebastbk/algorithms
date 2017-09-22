def len_lt(generator, n):
    for i, _ in enumerate(generator):
        if i >= n:
            return False
    return True


def len_lte(generator, n):
    for i, _ in enumerate(generator):
        if i > n:
            return False
    return True


def len_eq(generator, n):
    for i, _ in enumerate(generator):
        if i > n:
            return False
    return i < n


def len_gt(generator, n):
    for i, _ in enumerate(generator):
        if i > n:
            return True
    return False


def len_gte(generator, n):
    for i, _ in enumerate(generator):
        if i >= n:
            return True
    return False
