### Hexlet tests and linter status:
[![Actions Status](https://github.com/Chalo-nov/python-project-140/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Chalo-nov/python-project-140/actions)

[![Code Climate](https://codeclimate.com/github/Chalo-nov/python-project-140/badges/gpa.svg)](https://codeclimate.com/github/Chalo-nov/python-project-140)

## Demostración del Juego Brain Even (Paridad)

Aquí se muestra la instalación, ejecución y las dinámicas de victoria y derrota del juego:

[![Asciicast](https://asciinema.org/a/XqYg3WiHhI6aB6wfjn5QlHjE6.svg)](https://asciinema.org/a/XqYg3WiHhI6aB6wfjn5QlHjE6)


##  Demostración del Juego Brain Calc (Calculadora)

Este juego presenta al usuario una expresión matemática aleatoria (+, -, *). El jugador debe responder con el resultado correcto.

[![Asciicast](https://asciinema.org/a/44nOtNfmAk9ljlRpegPsywrRU.svg)](https://asciinema.org/a/44nOtNfmAk9ljlRpegPsywrRU)

##  Demostración del Juego Brain Gcd (Máximo Común Divisor)

Este juego presenta al usuario dos números y le pide encontrar el Máximo Común Divisor (MCD) de ambos.

[![Asciicast](https://asciinema.org/a/LLglXnKRylGSb1IQCPLeU6scM.svg)](https://asciinema.org/a/LLglXnKRylGSb1IQCPLeU6scM)

## Demostración del Juego Brain Progression

Este juego presenta al usuario una progresión aritmética con un número faltante (`..`), y el jugador debe identificar el valor correcto.

[![Asciicast](https://asciinema.org/a/ZT2ABVuD7xUn3TqQR2KbrTowX.svg)](https://asciinema.org/a/ZT2ABVuD7xUn3TqQR2KbrTowX)

## Demostración del Juego Brain Prime (Número Primo)

Este juego pide al usuario responder 'yes' si el número es primo, o 'no' si no lo es.

[![Asciicast](https://asciinema.org/a/Y1sr1jfkeDQV6kDiALV2fBuMX.svg)](https://asciinema.org/a/Y1sr1jfkeDQV6kDiALV2fBuMX)


##  Requisitos Mínimos

Para instalar y ejecutar este proyecto, necesitas tener instalado lo siguiente:

* **Python 3.8 o superior.**
* **La herramienta `uv`** (Usada para la gestión del entorno virtual y dependencias).

### Instalación del Entorno

Asegúrate de tener `uv` instalado globalmente (si es necesario) o sigue las instrucciones de la plataforma para configurarlo.

##  Instalación y Ejecución

Sigue estos pasos en tu terminal (se asume que usas WSL/Ubuntu con Python y Make instalados):

1.  **Instalar dependencias y crear el entorno virtual (.venv):**
    ```bash
    make install
    ```

2.  **Ejecutar un juego (Ejemplo: Brain Calc):**
    Para ejecutar cualquiera de los juegos, utiliza la regla `make` seguida del nombre del juego:
    ```bash
    make brain-calc
    # Para Brain Even:
    make brain-even
    # Para Brain Prime:
    make brain-prime