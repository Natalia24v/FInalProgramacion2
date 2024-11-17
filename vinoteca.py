import os
import json

# modelos
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class Vinoteca:
    __archivoDeDatos = "vinoteca.json"
    __bodegas = []
    __cepas = []
    __vinos = []

    @classmethod
    def inicializar(cls):
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)

    @classmethod
    def obtenerBodegas(cls, orden=None, reverso=False):
        if orden:
            return sorted(cls.__bodegas, key=lambda b: getattr(b, orden), reverse=reverso)
        return cls.__bodegas

    @classmethod
    def obtenerCepas(cls, orden=None, reverso=False):
        if orden:
            return sorted(cls.__cepas, key=lambda c: getattr(c, orden), reverse=reverso)
        return cls.__cepas

    @classmethod
    def obtenerVinos(cls, anio=None, orden=None, reverso=False):
        vinos_filtrados = cls.__vinos
        if anio:
            vinos_filtrados = [vino for vino in cls.__vinos if anio in vino.obtenerPartidas()]
        if orden:
            #diccionario para mapear los nombres de los atributos a los métodos correspondientes
            orden_map = {
                "id": "obtenerId",
                "nombre": "obtenerNombre",
                "bodega": "obtenerBodega",
                "partidas": "obtenerPartidas"
            }
            # Obtener el método correspondiente del diccionario
            metodo_orden = orden_map.get(orden)
            if metodo_orden:
                return sorted(vinos_filtrados, key=lambda v: getattr(v, metodo_orden)(), reverse=reverso)
        return vinos_filtrados

    @classmethod
    def buscarBodega(cls, id):
        return next((bodega for bodega in cls.__bodegas if bodega.obtenerId() == id), None)

    @classmethod
    def buscarCepa(cls, id):
        return next((cepa for cepa in cls.__cepas if cepa.obtenerId() == id), None)

    @classmethod
    def buscarVino(cls, id):
        return next((vino for vino in cls.__vinos if vino.obtenerId() == id), None)

    @classmethod
    def __parsearArchivoDeDatos(cls):
        with open(cls.__archivoDeDatos, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    @classmethod
    def __convertirJsonAListas(cls, datos):
        cls.__bodegas = [Bodega(**bodega) for bodega in datos['bodegas']]
        cls.__cepas = [Cepa(**cepa) for cepa in datos['cepas']]
        cls.__vinos = [Vino(**vino) for vino in datos['vinos']]