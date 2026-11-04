"""Punto de entrada principal de la simulación de la Planta Industrial.

Universidad de Burgos - Programación Modular y Orientada a Objetos
Curso 2026-2027
"""

from src.planta import PlantaIndustrial


def main():
    print("Iniciando aplicación de la Planta Industrial (POO)...")
    planta = PlantaIndustrial()
    planta.ejecutar()


if __name__ == "__main__":
    main()