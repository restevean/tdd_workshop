"""
Tests for the academic grading system.
The system converts numeric scores (0-10) to grades:
- 9-10: Outstanding
- 7-8.99: Notable
- 6-6.99: Good
- 5-5.99: Sufficient
- 3-4.99: Insufficient
- 0-2.99: Very poor
"""

from src.grading_system import grade_score


def test_grade_score_sobresaliente() -> None:
    """
    Test that verifies that a score of 9.5 is classified as Outstanding and passes.

    Given: A score of 9.5 points
    When: We classify the score
    Then: It should return ("Sobresaliente", True)
    """
    # Arrange
    score = 9.5
    expected_grade = "Sobresaliente"
    expected_passed = True

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_notable() -> None:
    """
    Test that verifies that a score of 8.0 is classified as Notable and passes.

    Given: A score of 8.0 points
    When: We classify the score
    Then: It should return ("Notable", True)
    """
    # Arrange
    score = 8.0
    expected_grade = "Notable"
    expected_passed = True

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_bien() -> None:
    """
    Test that verifies that a score of 6.5 is classified as Good and passes.

    Given: A score of 6.5 points
    When: We classify the score
    Then: It should return ("Bien", True)
    """
    # Arrange
    score = 6.5
    expected_grade = "Bien"
    expected_passed = True

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_suficiente() -> None:
    """
    Test that verifies that a score of 5.5 is classified as Sufficient and passes.

    Given: A score of 5.5 points
    When: We classify the score
    Then: It should return ("Suficiente", True)
    """
    # Arrange
    score = 5.5
    expected_grade = "Suficiente"
    expected_passed = True

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_insuficiente() -> None:
    """
    Test that verifies that a score of 4.0 is classified as Insufficient and does not pass.

    Given: A score of 4.0 points
    When: We classify the score
    Then: It should return ("Insuficiente", False)
    """
    # Arrange
    score = 4.0
    expected_grade = "Insuficiente"
    expected_passed = False

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_muy_deficiente() -> None:
    """
    Test that verifies that a score of 2.0 is classified as Very poor and does not pass.

    Given: A score of 2.0 points
    When: We classify the score
    Then: It should return ("Muy deficiente", False)
    """
    # Arrange
    score = 2.0
    expected_grade = "Muy deficiente"
    expected_passed = False

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_limite_sobresaliente() -> None:
    """
    Test that verifies the lower limit of Outstanding (exactly 9.0).

    Given: A score of 9.0 points (limit)
    When: We classify the score
    Then: It should return ("Sobresaliente", True)
    """
    # Arrange
    score = 9.0
    expected_grade = "Sobresaliente"
    expected_passed = True

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_limite_notable() -> None:
    """
    Test that verifies the lower limit of Notable (exactly 7.0).

    Given: A score of 7.0 points (limit)
    When: We classify the score
    Then: It should return ("Notable", True)
    """
    # Arrange
    score = 7.0
    expected_grade = "Notable"
    expected_passed = True

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_limite_bien() -> None:
    """
    Test that verifies the lower limit of Good (exactly 6.0).

    Given: A score of 6.0 points (limit)
    When: We classify the score
    Then: It should return ("Bien", True)
    """
    # Arrange
    score = 6.0
    expected_grade = "Bien"
    expected_passed = True

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_limite_aprobado() -> None:
    """
    Test that verifies the minimum limit to pass (exactly 5.0).

    Given: A score of 5.0 points (bare pass)
    When: We classify the score
    Then: It should return ("Suficiente", True)
    """
    # Arrange
    score = 5.0
    expected_grade = "Suficiente"
    expected_passed = True

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_limite_insuficiente() -> None:
    """
    Test that verifies the upper limit of Insufficient (4.99).

    Given: A score of 4.99 points
    When: We classify the score
    Then: It should return ("Insuficiente", False)
    """
    # Arrange
    score = 4.99
    expected_grade = "Insuficiente"
    expected_passed = False

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_nota_perfecta() -> None:
    """
    Test that verifies the maximum score (10.0).

    Given: A score of 10.0 points
    When: We classify the score
    Then: It should return ("Sobresaliente", True)
    """
    # Arrange
    score = 10.0
    expected_grade = "Sobresaliente"
    expected_passed = True

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed


def test_grade_score_nota_minima() -> None:
    """
    Test that verifies the minimum score (0.0).

    Given: A score of 0.0 points
    When: We classify the score
    Then: It should return ("Muy deficiente", False)
    """
    # Arrange
    score = 0.0
    expected_grade = "Muy deficiente"
    expected_passed = False

    # Act
    grade, passed = grade_score(score)

    # Assert
    assert grade == expected_grade
    assert passed == expected_passed
