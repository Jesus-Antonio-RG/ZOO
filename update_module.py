# Este es tu módulo de UPDATE.
# Contiene la función que se encargará de actualizar un animal.

def mostrar_lista_habitats(habitats):
    """Función auxiliar para mostrar los hábitats disponibles."""
    if not habitats:
        print("[Info] No hay hábitats registrados.")
        return
    print("\n--- Lista de Hábitats Disponibles ---")
    for i, habitat in enumerate(habitats, start=1):
        # Asumimos que los hábitats son objetos con atributos .nombre y .clima
        print(f"  {i}) {habitat.nombre} (Clima: {habitat.clima})")

def funcion_actualizar_animal(animales, habitats):
    """
    Esta es la función principal de tu módulo.
    Recibe el diccionario de animales y la lista de hábitats para poder trabajar.
    """
    print("\n--- Módulo de Actualización de Animal ---")

    # 1. Pedir el ID del animal a modificar
    id_animal = input("Ingresa el ID del animal que deseas actualizar (ej. A1): ").strip()

    # 2. Buscar si el animal existe
    animal_a_actualizar = animales.get(id_animal)

    if not animal_a_actualizar:
        print(f"[Error] No se encontró ningún animal con el ID '{id_animal}'.")
        return # Termina la función si no se encuentra el animal

    # 3. Si existe, mostrar un sub-menú para elegir qué actualizar
    animal_nombre = animal_a_actualizar._nombre # Asumimos que el animal tiene un atributo ._nombre
    print(f"\n¿Qué deseas actualizar de '{animal_nombre}' (ID: {id_animal})?")
    print("  1) Nombre")
    print("  2) Edad")
    print("  3) Hábitat")
    opcion = input("Elige una opción (o presiona Enter para cancelar): ").strip()

    # 4. Procesar la elección del usuario
    if opcion == "1":
        nuevo_nombre = input("Ingresa el nuevo nombre: ").strip()
        if nuevo_nombre:
            animal_a_actualizar._nombre = nuevo_nombre
            print(f"✅ Nombre actualizado a '{nuevo_nombre}'.")
        else:
            print("[Info] El nombre no puede estar vacío. Operación cancelada.")

    elif opcion == "2":
        try:
            nueva_edad = int(input("Ingresa la nueva edad: "))
            if nueva_edad >= 0:
                animal_a_actualizar._edad = nueva_edad # Asumimos que tiene un atributo ._edad
                print(f"✅ Edad actualizada a {nueva_edad} años.")
            else:
                print("[Error] La edad no puede ser negativa.")
        except ValueError:
            print("[Error] Edad inválida. Debe ser un número.")

    elif opcion == "3":
        mostrar_lista_habitats(habitats)
        try:
            indice_habitat = int(input("Elige el número del nuevo hábitat: "))
            if 1 <= indice_habitat <= len(habitats):
                nuevo_habitat = habitats[indice_habitat - 1]
                animal_a_actualizar.habitat = nuevo_habitat # Asumimos que tiene un atributo .habitat
                print(f"✅ Hábitat actualizado a '{nuevo_habitat.nombre}'.")
            else:
                print("[Error] Número de hábitat fuera de rango.")
        except (ValueError, IndexError):
            print("[Error] Selección inválida.")

    else:
        print("[Info] Operación de actualización cancelada.")

# NOTA: Este archivo por sí solo no se puede ejecutar y que funcione,
# porque necesita que el programa principal le pase la lista de 'animales' y 'habitats'.