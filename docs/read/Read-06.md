# Read-06 — Leer por ID (existe) con 'Hacer sonar'

## Objetivo
Evidenciar la lectura puntual de un animal existente por ID y la salida de `hacer_sonido()`.

## Métodos del código referenciados
- App._pedir_animal()
- Animal.hacer_sonido()

## Pasos para reproducir
1) Ejecutar el programa.
2) Elegir **5) Hacer sonar (animal)**.
3) Introducir un ID válido (ej. **A1**).

## Salida de consola
ID del animal (ej. A1): A1
Simba dice: ¡Roooaaar!

## Notas
`_pedir_animal()` lee el ID y, si existe en `zoo.animales`, invoca `hacer_sonido()` de la clase concreta (León/Tigre/Águila/Pingüino/Serpiente/Tortuga).
