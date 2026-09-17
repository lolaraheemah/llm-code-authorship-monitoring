def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


# Example
number = 29
print(is_prime(number))  # True