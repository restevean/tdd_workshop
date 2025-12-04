"""
Test for the sum function.
This is the first test following TDD - RED cycle.
"""

from src.calculator import add


def test_add_two_positive_numbers() -> None:
    """
    Test that verifies the add function correctly sums two positive numbers.

    Given: Two positive numbers (2 and 3)
    When: We sum them using the add function
    Then: The result should be 5
    """
    # Arrange
    number_a = 2
    number_b = 3
    expected_result = 5

    # Assert
    assert expected_result == add(number_a, number_b)


def test_add_negative_numbers() -> None:
    """
    Test that verifies the add function correctly sums two negative numbers.

    Given: Two negative numbers (-5 and -3)
    When: We sum them using the add function
    Then: The result should be -8
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
    Test that verifies the add function sums a positive and a negative number.

    Given: A positive number (10) and a negative number (-3)
    When: We sum them using the add function
    Then: The result should be 7
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
    Test that verifies the add function correctly sums when one of the numbers is zero.

    Given: A number (5) and zero (0)
    When: We sum them using the add function
    Then: The result should be 5
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
    Test that verifies the add function correctly sums decimal numbers.

    Given: Two decimal numbers (2.5 and 3.7)
    When: We sum them using the add function
    Then: The result should be 6.2
    """
    # Arrange
    number_a = 2.5
    number_b = 3.7
    expected_result = 6.2

    # Act
    result = add(number_a, number_b)

    # Assert
    assert result == expected_result
