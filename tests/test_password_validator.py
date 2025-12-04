from src.password_validator import validate_password


def test_password_too_short() -> None:
    """
    Test that verifies that a password with fewer than 8 characters is invalid.

    Given: A password of 6 characters "Abc12!"
    When: We validate the password
    Then: The result should be False
    """
    # Arrange
    password = "Abc12!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_valid_with_all_requirements() -> None:
    """
    Test that verifies that a password that meets all requirements is valid.

    Given: A password "Abc12345!" that meets all requirements.
    When: We validate the password.
    Then: The result should be True
    """
    # Arrange
    password = "Abc12345!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is True


def test_password_without_uppercase() -> None:
    """
    Test that verifies that a password without an uppercase letter is invalid.

    Given: A password "abc12345!" without uppercase letters
    When: We validate the password
    Then: The result should be False
    """
    # Arrange
    password = "abc12345!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_without_lowercase() -> None:
    """
    Test that verifies that a password without a lowercase letter is invalid.

    Given: A password "ABC12345!" without lowercase letters
    When: We validate the password
    Then: The result should be False
    """
    # Arrange
    password = "ABC12345!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_without_digit() -> None:
    """
    Test that verifies that a password without digits is invalid.

    Given: A password "Abcdefgh!" without numbers
    When: We validate the password
    Then: The result should be False
    """
    # Arrange
    password = "Abcdefgh!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_without_special_character() -> None:
    """
    Test that verifies that a password without a special character is invalid.

    Given: A password "Abc12345" without special characters
    When: We validate the password
    Then: The result should be False
    """
    # Arrange
    password = "Abc12345"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_exactly_8_characters() -> None:
    """
    Test that verifies that a password of exactly 8 characters is valid.

    Given: A password "Abc1234!" of exactly 8 characters
    When: We validate the password
    Then: The result should be True
    """
    # Arrange
    password = "Abc1234!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is True


def test_password_empty() -> None:
    """
    Test that verifies that an empty password is invalid.

    Given: An empty password ""
    When: We validate the password
    Then: The result should be False
    """
    # Arrange
    password = ""

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_with_multiple_special_characters() -> None:
    """
    Test that verifies that a password with multiple special characters is valid.

    Given: A password "Abc123!@#" with multiple special characters
    When: We validate the password
    Then: The result should be True
    """
    # Arrange
    password = "Abc123!@#"

    # Act
    result = validate_password(password)

    # Assert
    assert result is True
