def validate_password(password: str) -> bool:
    """
    Validates a password based on standard security criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (non-alphanumeric, non-space)
    
    Args:
        password (str): The password string to validate.
        
    Returns:
        bool: True if the password meets all criteria, False otherwise.
    """
    if not isinstance(password, str):
        return False
        
    if len(password) < 8:
        return False
        
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() and not char.isspace() for char in password)
    
    return all([has_upper, has_lower, has_digit, has_special])

# Example usage
if __name__ == "__main__":
    test_passwords = [
        "Secure@Pass123",  # Valid: has all required elements
        "short1!",         # Invalid: less than 8 characters
        "NoSpecialChar1",  # Invalid: lacks special character
        "nouppercase1!",   # Invalid: lacks uppercase letter
        "NOLOWERCASE1!",   # Invalid: lacks lowercase letter
        "NoDigitsHere!!",  # Invalid: lacks a digit
        "       !",        # Invalid: spaces don't count as valid letters/digits
        123456789          # Invalid: edge case handling for wrong type
    ]
    
    for pwd in test_passwords:
        result = validate_password(pwd)
        print(f"Password: {repr(pwd):<18} | Valid: {result}")