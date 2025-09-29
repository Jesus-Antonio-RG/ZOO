# =========================
#  Clases de dominio
# =========================
class Habitat:
    """Representa el hábitat de un animal en el zoo."""
    def __init__(self, nombre: str, clima: str):
        self.nombre = nombre
        self.clima = clima

    def describir(self) -> str:
        return f"Habitat(nombre='{self.nombre}', clima='{self.clima}')"

    def __repr__(self) -> str:
        return self.describir()
