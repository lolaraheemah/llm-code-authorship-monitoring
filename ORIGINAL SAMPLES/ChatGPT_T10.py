def validate_password(password):
    """
    Validate a password based on common security requirements:
    - At least 8 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    """
    if not isinstance(password, str):
        return False

    if len(password) < 8:
        return False

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    return has_upper and has_lower and has_digit and has_special


# Example
password = "Secure@123"
print(validate_password(password))  # True