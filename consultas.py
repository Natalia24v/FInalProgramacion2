from vinoteca import Vinoteca

#Clase que centraliza las consultas realizadas a la vinoteca.
class ConsultasVinoteca:
    @staticmethod
    def obtener_vinos_por_anio(anio, orden=None, reverso=False):
        #Obtiene la lista de vinos filtrada por año, ordenada si corresponde.
        return Vinoteca.obtenerVinos(anio=anio, orden=orden, reverso=reverso)

    @staticmethod
    def buscar_bodega_por_id(id):
        #Busca una bodega por su ID.
        return Vinoteca.buscarBodega(id)

    @staticmethod
    def obtener_bodegas(orden=None, reverso=False):
        #Obtiene la lista de bodegas ordenada si se especifica.
        return Vinoteca.obtenerBodegas(orden=orden, reverso=reverso)

    @staticmethod
    def obtener_cepas(orden=None, reverso=False):
        #Obtiene la lista de cepas ordenada si se especifica.
        return Vinoteca.obtenerCepas(orden=orden, reverso=reverso)

    @staticmethod
    def buscar_cepa_por_id(id):
        #Busca una cepa por su ID.
        return Vinoteca.buscarCepa(id)

    @staticmethod
    def buscar_vino_por_id(id):
        #Busca un vino por su ID.
        return Vinoteca.buscarVino(id)
