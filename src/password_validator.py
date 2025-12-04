"""Password validation with security requirements."""

import re

# Constants for validation patterns
MIN_LENGTH = 8
UPPERCASE_PATTERN = r"[A-Z]"
LOWERCASE_PATTERN = r"[a-z]"
DIGIT_PATTERN = r"\d"
SPECIAL_CHAR_PATTERN = r"[!@#$%^&*]"


def validate_password(password: str) -> bool:
    """
    Validate that a password meets all security requirements.

    Requirements:
    - At least 8 characters in length
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character (!@#$%^&*)

    Args:
        password (str): The password to validate

    Returns:
        bool: True if the password is valid, False otherwise
    """
    # Check minimum length
    if len(password) < MIN_LENGTH:
        return False

    # Check for at least one uppercase letter
    if not re.search(UPPERCASE_PATTERN, password):
        return False

    # Check for at least one lowercase letter
    if not re.search(LOWERCASE_PATTERN, password):
        return False

    # Check for at least one digit
    if not re.search(DIGIT_PATTERN, password):
        return False

    # Check for at least one special character
    if not re.search(SPECIAL_CHAR_PATTERN, password):
        return False

    # If all validations pass, the password is valid
    return True
