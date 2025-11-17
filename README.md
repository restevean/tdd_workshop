# TDD Workshop

Taller práctico de Test-Driven Development (TDD) con Python.

## Objetivos

- Aprender y practicar el ciclo Red-Green-Refactor
- Dominar pytest para testing en Python
- Aplicar TDD en ejercicios progresivos
- Integrar buenas prácticas de desarrollo

## Requisitos

- macOS Tahoe 26.1
- Python 3.12
- PyCharm (última versión)
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
