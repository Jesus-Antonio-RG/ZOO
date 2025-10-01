class Zoo:
    # UML: AGREGACIÓN (Aggregation):
    def _init_(self, nombre: str):
        self.nombre = nombre
        self.animales = {}      # UML: Aggregation (Zoo contiene muchos Animal)
        self.habitats = []      # UML: Aggregation (Zoo administra varios Habitat)
        self.personal = []      # UML: Aggregation (Zoo emplea cuidadores)