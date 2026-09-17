def is_prime(n: int) -> bool:
    """
    Determine if a given integer is a prime number.
    Returns False for numbers less than 2.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for factors from 5 up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

# Example usage:
if __name__ == "__main__":
    test_cases = [-5, 0, 1, 2, 3, 4, 17, 25, 97, 100]
    
    print("Prime Number Check Results:")
    for number in test_cases:
        print(f"{number:>3} -> {is_prime(number)}")