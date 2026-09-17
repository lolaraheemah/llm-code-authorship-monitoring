import re


def verify_email(email):
    """
    Verify whether an email address has a valid basic format.

    Returns True if valid, otherwise False.
    """
    if not isinstance(email, str):
        return False

    email = email.strip()

    if len(email) > 254:
        return False

    pattern = r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$"

    if not re.fullmatch(pattern, email):
        return False

    local, domain = email.rsplit("@", 1)

    # Local part cannot start or end with a dot or contain consecutive dots.
    if local.startswith(".") or local.endswith(".") or ".." in local:
        return False

    # Domain labels cannot start/end with a hyphen.
    for label in domain.split("."):
        if label.startswith("-") or label.endswith("-"):
            return False

    return True


# Example
email = "example@gmail.com"
print(verify_email(email))  # True