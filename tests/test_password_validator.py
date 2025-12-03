# tests/test_password_validator.py

from src.password_validator import validate_password


def test_password_too_short() -> None:
    """
    Test que verifica que una contraseña con menos de 8 caracteres es inválida.

    Dado: Una contraseña de 6 caracteres "Abc12!"
    Cuando: Validamos la contraseña
    Entonces: El resultado debe ser False
    """
    # Arrange
    password = "Abc12!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_valid_with_all_requirements() -> None:
    """
    Test que verifica que una contraseña que cumple todos los requisitos es válida.

    Dado: Una contraseña "Abc12345!" que cumple todos los requisitos.
    Cuando: Validamos la contraseña.
    Entonces: El resultado debe ser True
    """
    # Arrange
    password = "Abc12345!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is True


def test_password_without_uppercase() -> None:
    """
    Test que verifica que una contraseña sin letra mayúscula es inválida.

    Dado: Una contraseña "abc12345!" sin mayúsculas
    Cuando: Validamos la contraseña
    Entonces: El resultado debe ser False
    """
    # Arrange
    password = "abc12345!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_without_lowercase() -> None:
    """
    Test que verifica que una contraseña sin letra minúscula es inválida.

    Dado: Una contraseña "ABC12345!" sin minúsculas
    Cuando: Validamos la contraseña
    Entonces: El resultado debe ser False
    """
    # Arrange
    password = "ABC12345!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_without_digit() -> None:
    """
    Test que verifica que una contraseña sin dígitos es inválida.

    Dado: Una contraseña "Abcdefgh!" sin números
    Cuando: Validamos la contraseña
    Entonces: El resultado debe ser False
    """
    # Arrange
    password = "Abcdefgh!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_without_special_character() -> None:
    """
    Test que verifica que una contraseña sin carácter especial es inválida.

    Dado: Una contraseña "Abc12345" sin caracteres especiales
    Cuando: Validamos la contraseña
    Entonces: El resultado debe ser False
    """
    # Arrange
    password = "Abc12345"

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_exactly_8_characters() -> None:
    """
    Test que verifica que una contraseña de exactamente 8 caracteres es válida.

    Dado: Una contraseña "Abc1234!" de exactamente 8 caracteres
    Cuando: Validamos la contraseña
    Entonces: El resultado debe ser True
    """
    # Arrange
    password = "Abc1234!"

    # Act
    result = validate_password(password)

    # Assert
    assert result is True


def test_password_empty() -> None:
    """
    Test que verifica que una contraseña vacía es inválida.

    Dado: Una contraseña vacía ""
    Cuando: Validamos la contraseña
    Entonces: El resultado debe ser False
    """
    # Arrange
    password = ""

    # Act
    result = validate_password(password)

    # Assert
    assert result is False


def test_password_with_multiple_special_characters() -> None:
    """
    Test que verifica que una contraseña con varios caracteres especiales es válida.

    Dado: Una contraseña "Abc123!@#" con múltiples caracteres especiales
    Cuando: Validamos la contraseña
    Entonces: El resultado debe ser True
    """
    # Arrange
    password = "Abc123!@#"

    # Act
    result = validate_password(password)

    # Assert
    assert result is True
