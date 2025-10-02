class ReptilGenerico(Reptil):      # UML: Generalization ReptilGenerico —|> Reptil
    def _init(self, id, nombre, edad, categoria, habitat, especie: str):
        super()._init(id, nombre, edad, categoria, habitat, especie)

    def hacer_sonido(self) -> str:
        return "…"