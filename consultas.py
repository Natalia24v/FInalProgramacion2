from vinoteca import Vinoteca

#Clase que centraliza las consultas realizadas a la vinoteca.
class ConsultasVinoteca:
   #Obtiene la lista de vinos filtrada por año, ordenada si corresponde.
    @staticmethod
    def obtener_vinos_por_anio(anio, orden=None, reverso=False):
        
        return Vinoteca.obtenerVinos(anio=anio, orden=orden, reverso=reverso)

    #Busca una bodega por su ID.
    @staticmethod
    def buscar_bodega_por_id(id):
        return Vinoteca.buscarBodega(id)
    
    #Obtiene la lista de bodegas ordenada si se especifica.
    @staticmethod
    def obtener_bodegas(orden=None, reverso=False):
        return Vinoteca.obtenerBodegas(orden=orden, reverso=reverso)

    #Obtiene la lista de cepas ordenada si se especifica.
    @staticmethod
    def obtener_cepas(orden=None, reverso=False):
        return Vinoteca.obtenerCepas(orden=orden, reverso=reverso)

    #Busca una cepa por su ID.
    @staticmethod
    def buscar_cepa_por_id(id):
        return Vinoteca.buscarCepa(id)

    #Busca un vino por su ID.
    @staticmethod
    def buscar_vino_por_id(id):
        return Vinoteca.buscarVino(id)
