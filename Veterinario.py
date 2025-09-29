class Veterinario(IAtiendeAnimal):  # UML: Realization Veterinario ..|> IAtiendeAnimal
    # Además, Veterinario DEPENDE de Animal (parámetro en revisar/vacunar/atender).
    def _init_(self, nombre: str, especialidad: str):
        self.nombre = nombre
        self.especialidad = especialidad

    def revisar(self, a: Animal) -> None:   # UML: Dependency Veterinario ..> Animal
        print(f"[Vet {self.nombre}] Revisando a {a._nombre}… OK.")

    def vacunar(self, a: Animal) -> None:   # UML: Dependency Veterinario ..> Animal
        print(f"[Vet {self.nombre}] Vacunando a {a._nombre}… ¡Listo!")

    def atender(self, a: Animal) -> None:   # UML: Realization + Dependency ..> Animal
        print(f"[Vet {self.nombre}] Atendiendo a {a._nombre}