"""
Módulo de sistema de calificaciones académicas.
Clasifica notas numéricas (0-10) según el sistema español.
"""


def grade_score(score: float) -> tuple:
    """
    Clasifica una nota numérica según el sistema de calificación español.

    Rangos de calificación:
    - 9-10: Sobresaliente
    - 7-8.99: Notable
    - 6-6.99: Bien
    - 5-5.99: Suficiente
    - 3-4.99: Insuficiente
    - 0-2.99: Muy deficiente

    Args:
        score (float): Nota numérica entre 0 y 10

    Returns:
        tuple: (calificación, aprobado)
            - calificación (str): Nombre de la calificación
            - aprobado (bool): True si la nota es >= 5.0, False en caso contrario
    """

    # Determinar la calificación según el rango
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

    # Determinar si aprueba (nota >= 5.0)
    passed = score >= 5.0

    return grade, passed
