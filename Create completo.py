# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from enum import Enum
import unicodedata

# =========================
#  <<enumeration>>
# =========================
class CategoriaAnimal(Enum):
    """Categorías principales de animales."""
    MAMIFERO = 1
    AVE = 2
    REPTIL = 3


# =========================
#  Interfaz (Contrato)
# =========================
class IAtiendeAnimal(ABC):
    """Interfaz para clases que pueden atender a un Animal (Veterinario, Cuidador)."""
    @abstractmethod
    def atender(self, a: "Animal") -> None:
        """Método para realizar una atención general al animal."""
        pass


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


class Animal(ABC):  # UML: <<abstract>>
    """Clase abstracta base para todos los animales del zoo."""
    # UML: Animal DEPENDE de CategoriaAnimal (atributo tipado)
    def __init__(self, id_: str, nombre: str, edad: int,
                 categoria: CategoriaAnimal, habitat: Habitat, especie: str | None = None):
        self.id = id_
        self._nombre = nombre
        self._edad = edad
        self.categoria = categoria      # UML: Dependency Animal ..> CategoriaAnimal
        self.habitat = habitat          # UML: Association Animal — Habitat
        self.especie = especie if especie else self.__class__.__name__

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def edad(self) -> int:
        return self._edad

    def set_edad(self, edad: int) -> None:
        if edad < 0:
            print("[Error] La edad no puede ser negativa.")
            return
        self._edad = edad

    def info(self) -> str:
        return (f"id={self.id}, animal={self.especie}, nombre='{self._nombre}', "
                f"edad={self._edad}, categoria={self.categoria.name}, habitat='{self.habitat.nombre}'")

    @abstractmethod
    def hacer_sonido(self) -> str:
        """Método abstracto para el sonido característico del animal."""
        pass

    def __repr__(self) -> str:
        return self.info()


# ===== Herencia (Generalization): subclases abstractas intermedias =====
class Mamifero(Animal):
    def __init__(self, id_, nombre, edad, categoria, habitat, especie=None):
        super().__init__(id_, nombre, edad, categoria, habitat, especie)
    
    @abstractmethod
    def hacer_sonido(self) -> str:
        pass


class Ave(Animal):
    def __init__(self, id_, nombre, edad, categoria, habitat, especie=None):
        super().__init__(id_, nombre, edad, categoria, habitat, especie)

    @abstractmethod
    def hacer_sonido(self) -> str:
        pass


class Reptil(Animal):
    def __init__(self, id_, nombre, edad, categoria, habitat, especie=None):
        super().__init__(id_, nombre, edad, categoria, habitat, especie)
        
    @abstractmethod
    def hacer_sonido(self) -> str:
        pass
