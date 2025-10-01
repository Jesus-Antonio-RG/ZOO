    def agregarAnimal(self, a: Animal) -> None:
        # Agregación efectiva
        if a.id in self.animales:
            print(f"[Zoo] Ya existe un animal con id '{a.id}'.")
            return
        self.animales[a.id] = a
        print(f"[Zoo] Animal agregado: {a.info()}")

    def listarAnimales(self):
        return list(self.animales.values())

    def actualizarAnimal(self, id_: str, nuevo_nombre=None, nueva_edad=None, nuevo_habitat=None) -> None:
        a = self.animales.get(id_)
        if not a:
            print(f"[Zoo] No se encontró animal con id '{id_}'.")
            return
        if nuevo_nombre:
            a._nombre = nuevo_nombre
        if nueva_edad is not None:
            a.set_edad(nueva_edad)
        if nuevo_habitat:
            a.habitat = nuevo_habitat
        print(f"[Zoo] Animal actualizado: {a.info()}")

    def eliminarAnimal(self, id_: str) -> None:
        if id_ in self.animales:
            eliminado = self.animales.pop(id_)
            print(f"[Zoo] Animal eliminado: {eliminado.info()}")
        else:
            print(f"[Zoo] No existe animal con id '{id_}'.")