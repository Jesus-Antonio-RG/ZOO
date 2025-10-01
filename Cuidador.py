class Cuidador(IAtiendeAnimal):  # UML: Realization Cuidador ..|> IAtiendeAnimal
    # Además, Cuidador DEPENDE de Animal y Alimento.
    def _init_(self, nombre: str, turno: str):
        self.nombre = nombre
        self.turno = turno

    def alimentar(self, a: Animal, al: Alimento) -> None:
        # UML: Dependency Cuidador ..> Animal y ..> Alimento
        print(f"[Cuidador {self.nombre}] Alimentando a {a._nombre} con {al.cantidad} de {al.tipo}.")
        al.proporcionar()

    def limpiarHabitat(self, h: Habitat) -> None:
        # UML: Dependency Cuidador ..> Habitat
        print(f"[Cuidador {self.nombre}] Limpiando hábitat '{h.nombre}'… ¡Limpio!")

    def atender(self, a: Animal) -> None:
        print(f"[Cuidador {self.nombre}] Atendiendo a {a._nombre}.")