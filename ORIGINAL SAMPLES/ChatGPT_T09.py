from math import sqrt
from collections import Counter


def solve(data):
    """
    Calculate common descriptive statistics for a sequence of numbers.

    Returns:
        {
            "count": number of values,
            "sum": total,
            "mean": arithmetic mean,
            "median": median,
            "mode": list of modes,
            "variance": population variance,
            "std_dev": population standard deviation,
            "min": minimum,
            "max": maximum,
            "range": range
        }
    """
    if not data:
        raise ValueError("Data must contain at least one value.")

    values = sorted(data)
    n = len(values)
    total = sum(values)
    mean = total / n

    if n % 2 == 1:
        median = values[n // 2]
    else:
        median = (values[n // 2 - 1] + values[n // 2]) / 2

    frequencies = Counter(values)
    highest_frequency = max(frequencies.values())

    if highest_frequency == 1:
        mode = []
    else:
        mode = sorted(
            value for value, frequency in frequencies.items()
            if frequency == highest_frequency
        )

    variance = sum((x - mean) ** 2 for x in values) / n
    std_dev = sqrt(variance)

    minimum = values[0]
    maximum = values[-1]

    return {
        "count": n,
        "sum": total,
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "std_dev": std_dev,
        "min": minimum,
        "max": maximum,
        "range": maximum - minimum,
    }


# Example
if __name__ == "__main__":
    data = [2, 4, 4, 6, 8]

    result = solve(data)

    for key, value in result.items():
        print(f"{key}: {value}")