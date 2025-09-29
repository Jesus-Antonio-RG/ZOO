# ===== Especies genéricas (para especie libre) =====
class MamiferoGenerico(Mamifero):  # UML: Generalization MamiferoGenerico —|> Mamifero
    def _init(self, id, nombre, edad, categoria, habitat, especie: str):
        super()._init(id, nombre, edad, categoria, habitat, especie)

    def hacer_sonido(self) -> str:
        return "…"
