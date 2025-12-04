# TDD Workshop

Taller práctico de Test-Driven Development (TDD) con Python.

## Objetivos

- Aprender y practicar el ciclo Red-Green-Refactor
- Dominar pytest para testing en Python
- Aplicar TDD en ejercicios progresivos
- Integrar buenas prácticas de desarrollo

## Requisitos

- Python 3.12
- UV (gestor de dependencias)

## Setup del proyecto

### 1. Instalar UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clonar y configurar el proyecto

```bash
cd tdd_workshop
uv sync
```

### 3. Instalar dependencias de desarrollo

```bash
uv sync --dev
```

### 4. Configurar pre-commit hooks

```bash
uv run pre-commit install
uv run pre-commit install --hook-type pre-push
```

## Ejecutar tests

```bash
# Todos los tests
uv run pytest

# Tests específicos
uv run pytest tests/test_ejemplo.py

# Con coverage
uv run pytest --cov=src
```

## Estructura del proyecto

```
tdd_workshop/
├── src/           # Código fuente
└── tests/         # Tests
```

## Ciclo TDD

1. **Red**: Escribir un test que falle
2. **Green**: Escribir el código mínimo para pasar el test
3. **Refactor**: Mejorar el código manteniendo los tests en verde

## Comandos útiles

```bash
# Formatear código
uv run black src tests

# Ordenar imports
uv run isort src tests

# Ejecutar hooks manualmente
uv run pre-commit run --all-files
```

## Ejercicios

Los ejercicios se irán añadiendo progresivamente durante el taller.

## Ejemplo que ilustra un las diferencias entre un código escrito con TDD y otro sin TDD

### Código sin TDD
/src/grading_system.py
### Código con TDD
/src/grading_system_no_tdd.py

### Comparación visual:

  | Aspecto          | Sin TDD       | Con TDD      |
  |------------------|---------------|--------------|
  | Líneas de código | ~40           | ~15          |
  | Complejidad      | Alta          | Baja         |
  | Tests escritos   | 0 (o después) | 14 (primero) |
  | Bugs conocidos   | Desconocidos  | 0            |
  | Mantenibilidad   | Difícil       | Fácil        |
  | Confianza        | Baja          | Alta         |

  El ciclo TDD que evita esto:

  Ciclo típico SIN TDD:

  1. Escribir código (con suposiciones)
  2. "Creo que funciona"
  3. Integrar
  4. Bug en producción
  5. "¿Por qué no lo testeamos antes?"

Ciclo con TDD (el que usaste):

  1. RED: Test falla → test_grade_score_sobresaliente()
  2. GREEN: Código mínimo → if score >= 9.0: grade = "Sobresaliente"
  3. REFACTOR: Mejorar sin romper tests
  4. Repetir
  5. Código simple, testeado y funcional

  Ejemplo real del proyecto:

  La función grade_score tiene 14 tests que cubren:
  - ✅ Cada categoría de calificación
  - ✅ Límites entre categorías (edge cases)
  - ✅ Nota mínima (0.0)
  - ✅ Nota máxima (10.0)
  - ✅ Estado de aprobado/desaprobado

  Sin TDD: Probablemente habrías olvidado testear:
  - El límite de 4.99 (Insuficiente)
  - El límite exacto de 5.0 (aprobado justo)
  - El límite exacto de 9.0 (Sobresaliente)

 ### Conclusión:

  Sin TDD:
  - Código complejo "por si acaso"
  - Features no solicitadas
  - Bugs ocultos
  - Difícil de cambiar

  Con TDD:
  - Código simple y directo
  - Solo lo necesario
  - Bugs detectados inmediatamente
  - Fácil de cambiar (refactoring seguro)

  TDD te fuerza a escribir código simple que resuelve el problema real, no el problema imaginario.

## Informe de la cobertura de los tests
Instalamos un paquete adicional si no está ya incluido en las dependencias de desarrollo:
```bash
uv add --dev pytest-cov
```
Ejecutamos los tests (con "uv run" si el entorno virtual no está activado y sin ello si está activado) con la opción de cobertura:
```bash
uv run pytest --cov=src
