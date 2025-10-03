class Alimento:
    """Representa el alimento proporcionado a un animal."""
    # UML: Clase usada como DEPENDENCIA desde Cuidador.alimentar(...)
    def __init__(self, tipo: str, cantidad: float):
        self.tipo = tipo
        self.cantidad = cantidad

    def proporcionar(self) -> None:
        print(f"[Alimento] Proporcionado: {self.cantidad} de {self.tipo}")

    def __repr__(self) -> str:
        return f"Alimento(tipo='{self.tipo}', cantidad={self.cantidad})"