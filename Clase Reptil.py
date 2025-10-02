class Reptil(Animal):
    def __init__(self, id_, nombre, edad, categoria, habitat, especie=None):
        super().__init__(id_, nombre, edad, categoria, habitat, especie)
        
    @abstractmethod
    def hacer_sonido(self) -> str:
        pass
