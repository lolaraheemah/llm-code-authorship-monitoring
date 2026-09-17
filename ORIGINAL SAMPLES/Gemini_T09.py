def calculate_statistics(data: list[float]) -> dict:
    """
    Calculates basic descriptive statistics for a list of numbers.
    
    Args:
        data (list[float]): A list of numerical values.
        
    Returns:
        dict: A dictionary containing the mean, median, mode, sample variance, 
              and sample standard deviation. Returns an empty dictionary if data is empty.
    """
    if not data:
        return {}

    n = len(data)
    
    # Mean
    mean = sum(data) / n
    
    # Median
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    else:
        median = float(sorted_data[mid])
        
    # Mode
    frequency = {}
    for num in data:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    
    # If all numbers appear exactly once, standard convention often says there is no mode.
    if max_freq == 1 and n > 1:
        modes = []
    else:
        modes = [k for k, v in frequency.items() if v == max_freq]
        
    # Sample Variance and Sample Standard Deviation
    if n > 1:
        variance = sum((x - mean) ** 2 for x in data) / (n - 1)
        std_dev = variance ** 0.5
    else:
        variance = 0.0
        std_dev = 0.0
        
    return {
        'mean': mean,
        'median': median,
        'mode': modes,
        'sample_variance': variance,
        'sample_std_dev': std_dev
    }

if __name__ == "__main__":
    # Example usage
    dataset = [10.5, 12.0, 15.5, 10.5, 18.0, 22.5, 12.0, 10.5]
    
    stats = calculate_statistics(dataset)
    
    print("Dataset:", dataset)
    print("Statistics:")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"  {key.replace('_', ' ').title()}: {value:.4f}")
        else:
            print(f"  {key.replace('_', ' ').title()}: {value}")
            
    # Edge case: Empty list
    print("\nEmpty dataset stats:", calculate_statistics([]))
    
    # Edge case: Single element
    print("Single element stats:", calculate_statistics([42]))