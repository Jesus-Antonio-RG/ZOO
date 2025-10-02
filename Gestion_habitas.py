# --- Gestión hábitats / personal ---
    def agregarHabitat(self, h: Habitat) -> None:
        self.habitats.append(h)
        print(f"[Zoo] Hábitat agregado: {h.describir()}")

    def asignarHabitat(self, id_animal: str, h: Habitat) -> None:
        a = self.animales.get(id_animal)
        if not a:
            print(f"[Zoo] No se encontró animal con id '{id_animal}'.")
            return
        a.habitat = h
        print(f"[Zoo] Nuevo hábitat para {a._nombre}: '{h.nombre}'")

    def contratarCuidador(self, c: Cuidador) -> None:
        self.personal.append(c)
        print(f"[Zoo] Contratado cuidador: {c.nombre} (turno {c.turno})")