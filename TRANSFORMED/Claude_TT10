import re


def validate_password(password: str, min_length: int = 8) -> tuple[bool, list[str]]:
    """
    Validate a password against common security rules.

    Rules:
      - At least `min_length` characters long
      - Contains at least one uppercase letter
      - Contains at least one lowercase letter
      - Contains at least one digit
      - Contains at least one special character (non-alphanumeric)
      - Contains no whitespace

    Returns:
        (is_valid, list_of_error_messages)
    """
    errors = []

    if not isinstance(password, str) or password == "":
        return False, ["Password must be a non-empty string."]

    if len(password) < min_length:
        errors.append(f"Password must be at least {min_length} characters long.")

    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")

    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")

    if not re.search(r"\d", password):
        errors.append("Password must contain at least one digit.")

    if not re.search(r"[^A-Za-z0-9\s]", password):
        errors.append("Password must contain at least one special character.")

    if re.search(r"\s", password):
        errors.append("Password must not contain whitespace.")

    return (len(errors) == 0), errors


if __name__ == "__main__":
    test_passwords = [
        "Str0ng!Pass",
        "weak",
        "NoSpecialChar123",
        "no upper1!",
        "ALLUPPER1!",
        "",
        "Valid123!",
    ]

    for pwd in test_passwords:
        valid, issues = validate_password(pwd)
        print(f"Password: {pwd!r} -> Valid: {valid}")
        if not valid:
            for issue in issues:
                print(f"  - {issue}")