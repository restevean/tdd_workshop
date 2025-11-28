# tests/test_calculator.py

"""
Test para la función suma.
Este es el primer test siguiendo TDD - ciclo RED.
"""

from src.calculator import add


def test_add_two_positive_numbers() -> None:
    """
    Test que verifica que la función add suma correctamente dos números positivos.

    Dado: Dos números positivos (2 y 3)
    Cuando: Los sumamos usando la función add
    Entonces: El resultado debe ser 5
    """
    # Arrange (Preparar)
    number_a = 2
    number_b = 3
    expected_result = 5

    # Assert (Afirmar)
    assert expected_result == add(number_a, number_b)


def test_add_negative_numbers() -> None:
    """
    Test que verifica que la función add suma correctamente dos números negativos.

    Dado: Dos números negativos (-5 y -3)
    Cuando: Los sumamos usando la función add
    Entonces: El resultado debe ser -8
    """
    # Arrange
    number_a = -5
    number_b = -3
    expected_result = -8

    # Act
    result = add(number_a, number_b)

    # Assert
    assert result == expected_result


def test_add_positive_and_negative() -> None:
    """
    Test que verifica que la función add suma un número positivo y uno negativo.

    Dado: Un número positivo (10) y uno negativo (-3)
    Cuando: Los sumamos usando la función add
    Entonces: El resultado debe ser 7
    """
    # Arrange
    number_a = 10
    number_b = -3
    expected_result = 7

    # Act
    result = add(number_a, number_b)

    # Assert
    assert result == expected_result


def test_add_with_zero() -> None:
    """
    Test que verifica que la función add suma correctamente cuando uno de los números es cero.

    Dado: Un número (5) y cero (0)
    Cuando: Los sumamos usando la función add
    Entonces: El resultado debe ser 5
    """
    # Arrange
    number_a = 5
    number_b = 0
    expected_result = 5

    # Act
    result = add(number_a, number_b)

    # Assert
    assert result == expected_result


def test_add_decimal_numbers() -> None:
    """
    Test que verifica que la función add suma correctamente números decimales.

    Dado: Dos números decimales (2.5 y 3.7)
    Cuando: Los sumamos usando la función add
    Entonces: El resultado debe ser 6.2
    """
    # Arrange
    number_a = 2.5
    number_b = 3.7
    expected_result = 6.2

    # Act
    result = add(number_a, number_b)

    # Assert
    assert result == expected_result
