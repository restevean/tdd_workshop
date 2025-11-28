# src/password_validator.py

"""
Módulo de validación de contraseñas.
Verifica que las contraseñas cumplan con requisitos de seguridad.
"""

import re

# Constantes para los patrones de validación
MIN_LENGTH = 8
UPPERCASE_PATTERN = r"[A-Z]"
LOWERCASE_PATTERN = r"[a-z]"
DIGIT_PATTERN = r"\d"
SPECIAL_CHAR_PATTERN = r"[!@#$%^&*]"


def validate_password(password: str) -> bool:
    """
    Valida que una contraseña cumpla con todos los requisitos de seguridad.

    Requisitos:
    - Al menos 8 caracteres de longitud
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un dígito
    - Al menos un carácter especial (!@#$%^&*)

    Args:
        password (str): La contraseña a validar

    Returns:
        bool: True si la contraseña es válida, False en caso contrario
    """
    # Verificar longitud mínima
    if len(password) < MIN_LENGTH:
        return False

    # Verificar que contenga al menos una letra mayúscula
    if not re.search(UPPERCASE_PATTERN, password):
        return False

    # Verificar que contenga al menos una letra minúscula
    if not re.search(LOWERCASE_PATTERN, password):
        return False

    # Verificar que contenga al menos un dígito
    if not re.search(DIGIT_PATTERN, password):
        return False

    # Verificar que contenga al menos un carácter especial
    if not re.search(SPECIAL_CHAR_PATTERN, password):
        return False

    # Si pasa todas las validaciones, la contraseña es válida
    return True
