import re

def is_valid_email(email: str) -> bool:
    """
    Verifies if the given string is a valid email address format.
    """
    if not isinstance(email, str) or not email.strip():
        return False
        
    # A standard regular expression for validating email addresses
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    return bool(re.match(pattern, email))

if __name__ == "__main__":
    # Example usage
    test_emails = [
        "user@example.com",
        "firstname.lastname@domain.co.uk",
        "user+tag@custom-domain.org",
        "invalid_email.com",
        "missing@tld",
        "@no-username.com",
        " spaces @ example.com ",
        "",
        None
    ]
    
    for email in test_emails:
        status = "Valid" if is_valid_email(email) else "Invalid"
        print(f"{str(email):<30} -> {status}")