 @abstractmethod
    def hacer_sonido(self) -> str:
        """Método abstracto para el sonido característico del animal."""
        pass

    def __repr__(self) -> str:
        return self.info()