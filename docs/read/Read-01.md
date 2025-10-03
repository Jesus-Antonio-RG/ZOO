# Read-01 — Listar datos (bloque completo)

## Objetivo
Evidenciar la lectura global que hace el sistema al listar animales, hábitats, cuidadores y veterinarios.

## Métodos del código referenciados
- App._mostrar_listas()
- Zoo.listarAnimales()
- Animal.info()
- Habitat.describir()

## Pasos para reproducir
1) Ejecutar el programa.
2) Elegir la opción **1) Listar datos**.

## Salida de consola (arranque opcional)
[Zoo] Hábitat agregado: Habitat(nombre='Sabana', clima='Cálido seco')
[Zoo] Hábitat agregado: Habitat(nombre='Selva', clima='Húmedo tropical')
[Zoo] Hábitat agregado: Habitat(nombre='Montaña', clima='Frío')
[Zoo] Hábitat agregado: Habitat(nombre='Costa fría', clima='Frío oceánico')
[Zoo] Hábitat agregado: Habitat(nombre='Desierto rocoso', clima='Muy seco')
[Zoo] Hábitat agregado: Habitat(nombre='Pradera', clima='Templado seco')
[Zoo] Contratado cuidador: Ana (turno Mañana)
[Zoo] Contratado cuidador: Bruno (turno Tarde)
[Zoo] Animal agregado: id=A1, animal=León, nombre='Simba', edad=5, categoria=MAMIFERO, habitat='Sabana'
[Zoo] Animal agregado: id=A2, animal=Tigre, nombre='Shere Khan', edad=7, categoria=MAMIFERO, habitat='Selva'
[Zoo] Animal agregado: id=A3, animal=Águila, nombre='Skye', edad=3, categoria=AVE, habitat='Montaña'
[Zoo] Animal agregado: id=A4, animal=Pingüino, nombre='Pingo', edad=2, categoria=AVE, habitat='Costa fría'
[Zoo] Animal agregado: id=A5, animal=Serpiente, nombre='Sly', edad=4, categoria=REPTIL, habitat='Selva'
[Zoo] Animal agregado: id=A6, animal=Tortuga, nombre='Shelly', edad=80, categoria=REPTIL, habitat='Desierto rocoso'

[App] Datos de ejemplo cargados.

## Salida de consola (opción 1 — Listar datos)
== Animales ==
 - id=A1, animal=León, nombre='Simba', edad=5, categoria=MAMIFERO, habitat='Sabana'
 - id=A2, animal=Tigre, nombre='Shere Khan', edad=7, categoria=MAMIFERO, habitat='Selva'
 - id=A3, animal=Águila, nombre='Skye', edad=3, categoria=AVE, habitat='Montaña'
 - id=A4, animal=Pingüino, nombre='Pingo', edad=2, categoria=AVE, habitat='Costa fría'
 - id=A5, animal=Serpiente, nombre='Sly', edad=4, categoria=REPTIL, habitat='Selva'
 - id=A6, animal=Tortuga, nombre='Shelly', edad=80, categoria=REPTIL, habitat='Desierto rocoso'

== Hábitats ==
 1) Habitat(nombre='Sabana', clima='Cálido seco')
 2) Habitat(nombre='Selva', clima='Húmedo tropical')
 3) Habitat(nombre='Montaña', clima='Frío')
 4) Habitat(nombre='Costa fría', clima='Frío oceánico')
 5) Habitat(nombre='Desierto rocoso', clima='Muy seco')
 6) Habitat(nombre='Pradera', clima='Templado seco')

== Cuidadores ==
 1) Ana (turno Mañana)
 2) Bruno (turno Tarde)

== Veterinarios (asociados) ==
 1) Dra. Ruiz (esp. Fauna salvaje)
 2) Dr. López (esp. Reptiles)

## Notas
La data inicial proviene de `_cargar_datos_ejemplo()`. No se modifica la lógica del programa; solo se documenta la lectura que ya imprime el sistema.
