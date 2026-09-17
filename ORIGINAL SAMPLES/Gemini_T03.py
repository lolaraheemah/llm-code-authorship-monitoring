import re
from collections import Counter
from typing import Dict

def get_word_frequency(text: str) -> Dict[str, int]:
    """
    Calculates the frequency of words in a given text.
    Handles edge cases like empty inputs, non-string inputs, punctuation, and mixed casing.
    """
    if not isinstance(text, str) or not text.strip():
        return {}
    
    # Convert text to lowercase and extract words using regex
    # \b matches word boundaries, \w+ matches 1 or more alphanumeric characters
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count frequencies and return as a dictionary
    return dict(Counter(words))

# Example usage:
if __name__ == "__main__":
    sample_text = "Hello world! This is a test. Hello, this test is only a test."
    
    frequencies = get_word_frequency(sample_text)
    
    print("Sample Text:")
    print(sample_text)
    print("\nWord Frequencies:")
    
    # Sort by frequency (descending) and then alphabetically
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_frequencies:
        print(f"{word}: {count}")
        
    # Edge case examples
    print("\nEdge Case (Empty String):", get_word_frequency(""))
    print("Edge Case (Punctuation Only):", get_word_frequency("!!! ??? ,,, ..."))
    print("Edge Case (None Type):", get_word_frequency(None))