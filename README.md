# Práctica I: Refactorización de una Planta Industrial mediante Programación Orientada a Objetos (POO)

**Universidad de Burgos**  
**Asignatura:** Programación Modular y Orientada a Objetos  
**Curso:** 2026-2027  
**Realizado por Dario Gonzalez Moreno
---

## Descripción del Proyecto
Este proyecto consiste en la refactorización completa de una simulación realista de una planta industrial desarrollada en Python utilizando **MuJoCo**, **OpenCV** y **NumPy**. El código original implementaba una planta mediante programación procedural con funciones globales y compartidas. El objetivo de esta práctica es transformar dicha arquitectura en un diseño modular basado en **Programación Orientada a Objetos (POO)**, dotando a cada componente de responsabilidades claramente definidas, encapsulamiento y composición, sirviendo además como base extensible para la Práctica.

---

## Estructura del Proyecto
El proyecto sigue una organización modular limpia, separando el punto de entrada de la lógica de negocio ubicada en el directorio `src/`.

```text
planta_industrial/
├── main.py                  # Punto de entrada principal de la aplicación
├── requirements.txt         # Dependencias del software (MuJoCo, OpenCV, NumPy)
└── src/
    ├── __init__.py          # Inicializador del paquete modular
    ├── planta.py            # Clase coordinadora (PlantaIndustrial)
    ├── cinta_transportadora.py # Gestión independiente del estado de las cintas
    ├── camara_inspeccion.py # Adquisición visual, procesamiento OpenCV y parada automática
    ├── objeto_industrial.py # Modelado de piezas y geometrías industriales
    ├── horno.py             # Control térmico y actualización visual del color en MuJoCo
    └── robot.py             # Envoltorio para la cinemática inversa (IK) del robot Panda
