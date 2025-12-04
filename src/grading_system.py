"""
Academic grading system module.
Classifies numerical marks (0-10) according to the Spanish grading system.
"""


def grade_score(score: float) -> tuple:
    """
    Classify a numerical mark according to the Spanish grading system.

    Grading ranges:
    - 9-10: Sobresaliente (Outstanding)
    - 7-8.99: Notable (Very Good)
    - 6-6.99: Bien (Good)
    - 5-5.99: Suficiente (Pass)
    - 3-4.99: Insuficiente (Insufficient)
    - 0-2.99: Muy deficiente (Very Poor)

    Args:
        score (float): Numerical mark between 0 and 10

    Returns:
        tuple: (grade, passed)
            - grade (str): Name of the grade
            - passed (bool): True if the mark is >= 5.0, False otherwise
    """

    # Determine the grade according to the range
    if score >= 9.0:
        grade = "Sobresaliente"
    elif score >= 7.0:
        grade = "Notable"
    elif score >= 6.0:
        grade = "Bien"
    elif score >= 5.0:
        grade = "Suficiente"
    elif score >= 3.0:
        grade = "Insuficiente"
    else:
        grade = "Muy deficiente"

    # Determine if passed (mark >= 5.0)
    passed = score >= 5.0

    return grade, passed
