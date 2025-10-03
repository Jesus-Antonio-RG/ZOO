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