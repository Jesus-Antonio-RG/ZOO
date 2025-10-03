# Read-08 — Lectura de interacción: Alimentar

## Objetivo
Evidenciar los impresos/lecturas al alimentar (cuidador → animal).

## Métodos del código referenciados
- App._pedir_animal()
- App._primer_cuidador()
- Cuidador.alimentar()
- Alimento.proporcionar()

## Pasos para reproducir
1) Ejecutar el programa.
2) Elegir **6) Alimentar (cuidador → animal)**.
3) Introducir un ID válido (ej. **A2**).
4) Escribir tipo de alimento (ej. **Comida**).
5) Escribir cantidad (ej. **1.0**).

## Salida de consola (ejemplo)
ID del animal (ej. A1): A2
Tipo de alimento: Comida
Cantidad (solo número): 1.0
[Cuidador Ana] Alimentando a Shere Khan con 1.0 de Comida.
[Alimento] Proporcionado: 1.0 de Comida

## Notas
Se usa el primer cuidador de la lista (`Ana`) a través de `_primer_cuidador()`.  
No se modifica la lógica; solo se evidencia lo que imprime el sistema.
