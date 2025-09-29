@property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def edad(self) -> int:
        return self._edad

    def set_edad(self, edad: int) -> None:
        if edad < 0:
            print("[Error] La edad no puede ser negativa.")
            return
        self._edad = edad

    def info(self) -> str:
        return (f"id={self.id}, animal={self.especie}, nombre='{self._nombre}', "
                f"edad={self._edad}, categoria={self.categoria.name}, habitat='{self.habitat.nombre}'")