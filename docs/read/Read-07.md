# Read-07 — Leer por ID (no existe)

## Objetivo
Evidenciar el comportamiento de lectura cuando el ID de animal NO existe.

## Métodos del código referenciados
- App._pedir_animal()

## Pasos para reproducir
1) Ejecutar el programa.
2) Elegir **5) Hacer sonar (animal)** (o cualquier opción que pida ID).
3) Introducir un ID inexistente, por ejemplo **AXXX**.

## Salida de consola
ID del animal (ej. A1): AXXX
[Info] ID no encontrado.

## Notas
El mensaje lo imprime `_pedir_animal()` cuando `id_` no aparece en `zoo.animales`.
No se modifica lógica; solo se documenta la lectura que ya realiza el sistema.
