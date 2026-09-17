import math
from collections import Counter


def compute_statistics(data):
    """
    Compute basic descriptive statistics for a list of numbers.

    Parameters:
        data (list of int/float): Input numeric data.

    Returns:
        dict: Dictionary containing count, sum, mean, median, mode,
              variance, standard deviation, min, max, and range.

    Raises:
        ValueError: If data is empty or contains non-numeric values.
    """
    if not data:
        raise ValueError("Input data must not be empty.")

    for x in data:
        if not isinstance(x, (int, float)) or isinstance(x, bool):
            raise ValueError(f"Non-numeric value found: {x!r}")

    n = len(data)
    total = sum(data)
    mean = total / n

    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        median = sorted_data[mid]

    counts = Counter(data)
    max_count = max(counts.values())
    modes = sorted([k for k, v in counts.items() if v == max_count])
    mode = modes[0] if len(modes) == 1 else modes  # single value or list of ties

    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)

    data_min = min(data)
    data_max = max(data)
    data_range = data_max - data_min

    return {
        "count": n,
        "sum": total,
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "std_dev": std_dev,
        "min": data_min,
        "max": data_max,
        "range": data_range,
    }


if __name__ == "__main__":
    sample_data = [4, 8, 6, 5, 3, 8, 9, 8, 1, 7]
    stats = compute_statistics(sample_data)
    for key, value in stats.items():
        print(f"{key}: {value}")