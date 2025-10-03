# Read-09 — Lectura de interacción: Revisar y Vacunar

## Objetivo
Evidenciar los impresos que genera el sistema al **revisar** y **vacunar** un animal.

## Métodos del código referenciados
- App._pedir_animal()
- App._primer_veterinario()
- Veterinario.revisar()
- Veterinario.vacunar()

## Pasos para reproducir
1) Ejecutar el programa.
2) Elegir **7) Revisar (veterinario → animal)** e introducir un ID válido (ej. **A3**).
3) Elegir **8) Vacunar (veterinario → animal)** e introducir un ID válido (puede ser el mismo **A3**).

## Salida de consola (ejemplo)
# Revisar
ID del animal (ej. A1): A3
[Vet Dra. Ruiz] Revisando a Skye… OK.

# Vacunar
ID del animal (ej. A1): A3
[Vet Dra. Ruiz] Vacunando a Skye… ¡Listo!

## Notas
El veterinario usado es el primero disponible (`Dra. Ruiz`) mediante `_primer_veterinario()`.  
No se cambia lógica; únicamente se documenta la lectura impresa por el sistema.
