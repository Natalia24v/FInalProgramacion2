from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    def establecerNombre(self, nombre):
        self.__nombre = nombre

    def obtenerId(self):
        return self.__id

    def obtenerNombre(self):
        return self.__nombre

    # Sobrescribir Consulta __eq__ (compara por Id)
    def __eq__(self, otro_obj):
        if isinstance(otro_obj, EntidadVineria):
            return self.__id == otro_obj.__id
        return False

    # Convertir a JSON
    @abstractmethod
    def convertirAJSON(self):
        pass
