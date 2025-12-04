"""
Tests para el sistema de calificaciones académicas.
El sistema convierte notas numéricas (0-10) a calificaciones:
- 9-10: Sobresaliente
- 7-8.99: Notable
- 6-6.99: Bien
- 5-5.99: Suficiente
- 3-4.99: Insuficiente
- 0-2.99: Muy deficiente
"""

from src.grading_system import grade_score


def test_grade_score_sobresaliente() -> None:
    """
    Test que verifica que una nota de 9.5 se clasifica como Sobresaliente y aprueba.

    Dado: Una nota de 9.5 puntos
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Sobresaliente", True)
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
    Test que verifica que una nota de 8.0 se clasifica como Notable y aprueba.

    Dado: Una nota de 8.0 puntos
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Notable", True)
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
    Test que verifica que una nota de 6.5 se clasifica como Bien y aprueba.

    Dado: Una nota de 6.5 puntos
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Bien", True)
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
    Test que verifica que una nota de 5.5 se clasifica como Suficiente y aprueba.

    Dado: Una nota de 5.5 puntos
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Suficiente", True)
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
    Test que verifica que una nota de 4.0 se clasifica como Insuficiente y no aprueba.

    Dado: Una nota de 4.0 puntos
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Insuficiente", False)
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
    Test que verifica que una nota de 2.0 se clasifica como Muy deficiente y no aprueba.

    Dado: Una nota de 2.0 puntos
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Muy deficiente", False)
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
    Test que verifica el límite inferior del Sobresaliente (exactamente 9.0).

    Dado: Una nota de 9.0 puntos (límite)
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Sobresaliente", True)
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
    Test que verifica el límite inferior del Notable (exactamente 7.0).

    Dado: Una nota de 7.0 puntos (límite)
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Notable", True)
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
    Test que verifica el límite inferior del Bien (exactamente 6.0).

    Dado: Una nota de 6.0 puntos (límite)
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Bien", True)
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
    Test que verifica el límite mínimo para aprobar (exactamente 5.0).

    Dado: Una nota de 5.0 puntos (aprobado justo)
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Suficiente", True)
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
    Test que verifica el límite superior del Insuficiente (4.99).

    Dado: Una nota de 4.99 puntos
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Insuficiente", False)
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
    Test que verifica la nota máxima (10.0).

    Dado: Una nota de 10.0 puntos
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Sobresaliente", True)
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
    Test que verifica la nota mínima (0.0).

    Dado: Una nota de 0.0 puntos
    Cuando: Clasificamos la nota
    Entonces: Debe devolver ("Muy deficiente", False)
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
