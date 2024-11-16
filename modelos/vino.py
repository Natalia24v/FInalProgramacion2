import json
from entidadvineria import EntidadVineria
import vinoteca

class Vino (EntidadVineria):

    def __init__(self, id: str, nombre: str, bodega: str, cepas: list, partidas: list):
        super().__init__(id, nombre)
        self.__bodega = bodega
        self.__cepas = cepas
        self.__partidas = partidas

    def __repr__(self):
        return json.dumps({"nombre": self.obtenerNombre()})

    def convertirAJSON(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def convertirAJSONFull(self):
        return {
            "id": self.obtenerId(),
            "nombre": self.obtenerNombre(),
            "bodega": self.obtenerBodega().obtenerNombre(),
            "cepas": self.__mapearCepas(),
            "partidas": self.__partidas,
        }

    def __mapearCepas(self):
        cepas = self.obtenerCepas()
        cepasMapa = map(lambda a: a.obtenerNombre(), cepas)
        return list(cepasMapa)

# Código agregado
# La consulta obtenerBodega debe hacer uso del servicio buscarBodega de la clase Vinoteca para recuperar el objeto de tipo Bodega asociado al vino.
    def obtenerBodega(self):
        return vinoteca.Vinoteca.buscarBodega(self.__bodega)

# La consulta obtenerCepas puede hacer uso de los servicios buscarCepa u obtenerCepas de la clase Vinoteca para recuperar los objetos de tipo Cepa para las cepas en las que se ofrece el vino en cuestión.
    def obtenerCepas(self):
        return [vinoteca.Vinoteca.buscarCepa(cepa_id) for cepa_id in self.__cepas]

# Consulta obtenerPartidas    
    def obtenerPartidas(self):
        return self.__partidas