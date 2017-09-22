from utils.generators import len_eq


def factors(n):
    return list(yield_factors(n))


def yield_factors(n):
    for i in range(1, n+1):
        if n % i == 0:
            yield i


def prime_factors(n):
    return list(yield_prime_factors(n))


def yield_prime_factors(n):
    return (f for f in yield_factors(n) if is_prime(f))


def is_prime(n):
    if n < 2:
        return False
    return len_eq(yield_factors(n), 2)
