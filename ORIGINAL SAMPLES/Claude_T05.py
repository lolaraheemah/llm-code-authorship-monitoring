def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_up_to(limit: int) -> list:
    """Return a list of all prime numbers from 2 up to and including limit."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]


if __name__ == "__main__":
    print(is_prime(17))          # True
    print(is_prime(18))          # False
    print(primes_up_to(30))      # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]