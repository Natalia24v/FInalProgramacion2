import json

class Vinoteca:
    # Atributos de clase
    archivoDeDatos = "vinoteca.json"
    bodega = []
    cepa = []
    vino = []

    @classmethod
    def inicializar(cls):
        """
        Inicializa las colecciones de bodegas, cepas y vinos
        cargando la información desde el archivo JSON.
        """
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJSONaListas(datos)

    #Retorna la lista de cepas y bodegas, ordenada según los parámetros proporcionados.

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        if orden:
            return sorted(cls.bodega, key=lambda b: b[orden], reverse=reverso)
        return cls.bodega

    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        if orden:
            return sorted(cls.cepa, key=lambda c: c[orden], reverse=reverso)
        return cls.cepa

    #Retorna la lista de vinos, filtrada por año si se proporciona, y ordenada si corresponde.

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos_filtrados = cls.vino
        if anio:
            vinos_filtrados = [vino for vino in cls.vino if anio in vino.get("partidas", [])]
        if orden:
            return sorted(vinos_filtrados, key=lambda v: v[orden], reverse=reverso)
        return vinos_filtrados
    
    #Busca y retorna un vino por su ID. Retorna None si no se encuentra.

    @classmethod
    def buscarBodega(cls, id):
        return next((bodega for bodega in cls.bodega if bodega["id"] == id), None)

    @classmethod
    def buscarCepa(cls, id):
        return next((cepa for cepa in cls.cepa if cepa["id"] == id), None)

    @classmethod
    def buscarVino(cls, id):
        return next((vino for vino in cls.vino if vino["id"] == id), None)

    #Abre el archivo JSON, carga la información y la devuelve como un diccionario.

    @classmethod
    def __parsearArchivoDeDatos(cls):
        with open(cls.archivoDeDatos, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    
    #Convierte los datos JSON en listas para las colecciones de bodegas, cepas y vinos.

    @classmethod
    def __convertirJSONaListas(cls, listas):
        cls.bodega = listas.get("bodega", [])
        cls.cepa = listas.get("cepa", [])
        cls.vino = listas.get("vino", [])
    