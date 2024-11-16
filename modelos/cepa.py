import json
from entidadvineria import EntidadVineria
import vinoteca


class Cepa (EntidadVineria):

# Añadí el constructor que hereda de EntidadVineria para usar id y nombre.
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

# Código Agregado
# Consulta obtenerVinos
    def obtenerVinos(self):
        # La consulta obtenerVinos debe hacer uso del servicio obtenerVinos de la clase Vinoteca para recuperar todos los vinos contenidos en el archivo json. Sobre dicha lista se debe iterar hasta encontrar los vinos que se ofrecen en la cepa en cuestión.
        todos_los_vinos = vinoteca.Vinoteca.obtenerVinos(None, None, None)
        return [vino for vino in todos_los_vinos if self.obtenerId() in [cepa.obtenerId() for cepa in vino.obtenerCepas()]]