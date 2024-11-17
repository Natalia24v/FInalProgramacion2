import json
from entidadvineria import EntidadVineria
import vinoteca

class Cepa(EntidadVineria):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(
            lambda a: a.obtenerNombre()
            + " ("
            + a.obtenerBodega().obtenerNombre()
            + ")",
            vinos,
        )
        return list(vinosMapa)

    def obtenerVinos(self):
        todos_los_vinos = vinoteca.Vinoteca.obtenerVinos(None, None, None)
        return [vino for vino in todos_los_vinos if self.obtenerId() in [cepa.obtenerId() for cepa in vino.obtenerCepas()]]

    def __hash__(self):
        return hash(self.obtenerId())

    def __eq__(self, other):
        if isinstance(other, Cepa):
            return self.obtenerId() == other.obtenerId()
        return False
