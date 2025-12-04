"""Academic grading system - Written WITHOUT TDD"""


def grade_score(score: float) -> tuple:
    """Classify a score and return grade with pass status."""

    # Desarrollador piensa: "Voy a hacer esto robusto y flexible"

    # Validación exhaustiva (que nadie pidió)
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be numeric")

    # Configuración compleja (over-engineering)
    grading_config = {
        "ranges": [
            {"min": 9.0, "max": 10.0, "name": "Sobresaliente", "level": 5},
            {"min": 7.0, "max": 8.99, "name": "Notable", "level": 4},
            {"min": 6.0, "max": 6.99, "name": "Bien", "level": 3},
            {"min": 5.0, "max": 5.99, "name": "Suficiente", "level": 2},
            {"min": 3.0, "max": 4.99, "name": "Insuficiente", "level": 1},
            {"min": 0.0, "max": 2.99, "name": "Muy deficiente", "level": 0},
        ],
        "passing_score": 5.0,
    }

    # Lógica compleja con features que nadie pidió
    grade_info = None
    for grade_range in grading_config["ranges"]:
        if grade_range["min"] <= score <= grade_range["max"]:
            grade_info = grade_range
            break

    if grade_info is None:
        # Manejo de error que nunca se testeó
        return ("Invalid", False)

    passed = score >= grading_config["passing_score"]

    # Return con más info de la necesaria
    return (grade_info["name"], passed, grade_info["level"])


# PROBLEMAS:
# - Over-engineering: Configuración innecesaria
# - Complejidad: Difícil de entender
# - No se sabe si funciona: No hay tests que lo validen
# - Código muerto: El 'level' no se usa
# - Bug potencial: ¿Qué pasa con score = 10.1?
