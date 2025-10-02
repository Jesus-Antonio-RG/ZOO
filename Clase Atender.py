# =========================
#  Interfaz (Contrato)
# =========================
class IAtiendeAnimal(ABC):
    """Interfaz para clases que pueden atender a un Animal (Veterinario, Cuidador)."""
    @abstractmethod
    def atender(self, a: "Animal") -> None:
        """Método para realizar una atención general al animal."""
        pass