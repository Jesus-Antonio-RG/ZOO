def _sin_acentos(s: str) -> str:
    """Utilidad para comparar nombres de especie sin tildes (no afecta al UML)."""
    t = unicodedata.normalize("NFD", s)
    t = "".join(ch for ch in t if unicodedata.category(ch) != "Mn")
    return t.upper().strip()