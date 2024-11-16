import json
from entidadvineria import EntidadVineria
import vinoteca


class Bodega (EntidadVineria):
    
    def __repr__(self):
        return json.dumps(self.convertirAJSON())

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": len(self.obtenerVinos()),
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "vinos": self.__mapearVinos(),
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

    def __mapearVinos(self):
        vinos = self.obtenerVinos()
        vinosMapa = map(lambda a: a.obtenerNombre(), vinos)
        return list(vinosMapa)

# Código agregado
# Consulta obtenerVinos
    def obtenerVinos(self):
        # La consulta obtenerVinos debe hacer uso del servicio obtenerVinos de la clase Vinoteca para recuperar todos los vinos contenidos en el archivo json. Sobre dicha lista se debe iterar hasta encontrar los vinos que pertenecen a la bodega en cuestión.
        todos_ls_vinos = vinoteca.Vinoteca.obtenerVinos(None, None, None)
        return [vino for vino in todos_ls_vinos if vino.obtenerBodega().obtenerId() == self.obtenerId()]


# Consulta obtenerCepas
    def obtenerCepas(self):
        # La consulta obtenerCepas debe seguir la misma impronta que el punto anterior para intentar encontrar aquellos vinos que pertenecen a la bodega, recuperando únicamente las cepas en los que se ofrecen estos.
        vinos = self.obtenerVinos()
        cepas = set()
        for vino in vinos:
            for cepa in vino.obtenerCepas():
                cepas.add(cepa)
        return list(cepas)