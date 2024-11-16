from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def establecerNombre(self, nombre):
        self.nombre = nombre

    def obtenerId(self):
        return self.id

    def obtenerNombre(self):
        return self.nombre

    # Sobrescribir Consulta __eq__ (compara por Id)
    def __eq__(self, otro_obj):
        if isinstance(otro_obj, EntidadVineria):
            return self.id == otro_obj.id
        return False

    # Convertir a JSON
    @abstractmethod
    def convertirAJSON(self):
        pass
