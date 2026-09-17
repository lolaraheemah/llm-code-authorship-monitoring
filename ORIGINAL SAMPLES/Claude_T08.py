import re

def is_valid_email(email: str) -> bool:
    """
    Validate an email address format.

    Returns True if the email matches a reasonable standard format,
    False otherwise.
    """
    if not isinstance(email, str):
        return False

    email = email.strip()

    if not email or len(email) > 254:
        return False

    # Must have exactly one '@'
    if email.count('@') != 1:
        return False

    local_part, domain_part = email.split('@')

    if not local_part or not domain_part:
        return False

    if len(local_part) > 64:
        return False

    # Local part: letters, digits, and ._%+- (no leading/trailing dot, no consecutive dots)
    local_pattern = r'^[A-Za-z0-9](?:[A-Za-z0-9._%+-]*[A-Za-z0-9])?$'
    if '..' in local_part or not re.match(local_pattern, local_part):
        return False

    # Domain part: labels separated by dots, each label alphanumeric/hyphen,
    # no leading/trailing hyphen, must end with a valid TLD (letters only, 2+ chars)
    domain_pattern = (
        r'^(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+'
        r'[A-Za-z]{2,}$'
    )
    if '..' in domain_part or not re.match(domain_pattern, domain_part):
        return False

    return True


if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "first.last@sub.example.co.uk",
        "invalid@",
        "@invalid.com",
        "no_at_sign.com",
        "double..dot@example.com",
        "user@-invalid.com",
        "user@invalid-.com",
        "valid_email123@domain123.org",
        "",
        None,
    ]

    for e in test_emails:
        print(f"{e!r}: {is_valid_email(e)}")