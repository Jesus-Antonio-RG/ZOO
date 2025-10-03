# ===== Herencia (Generalization): especies concretas =====
class Leon(Mamifero):
    def hacer_sonido(self) -> str:
        return "¡Roooaaar!"


class Tigre(Mamifero):
    def hacer_sonido(self) -> str:
        return "¡Grrrr!"


class Aguila(Ave):
    def hacer_sonido(self) -> str:
        return "¡Screee!"


class Pinguino(Ave):
    def hacer_sonido(self) -> str:
        return "¡Honk-honk!"


class Serpiente(Reptil):
    def hacer_sonido(self) -> str:
        return "¡Sssss!"


class Tortuga(Reptil):
    def hacer_sonido(self) -> str:
        return "…"
