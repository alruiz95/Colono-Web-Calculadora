import pickle

"""
Clase reporte estructura de datos generales de la imagen.
"""


class Reporte:
    def __init__(self, escala, ruido, proximidad, capacidad, conteo, ciclos, tiempo, multiArchivo, nombreArchivo):
        self.escala = escala
        self.ruido = ruido
        self.proximidad = proximidad
        self.capacidad = capacidad
        self.conteo = conteo
        self.ciclos = ciclos
        self.tiempo = tiempo
        self.multiArchivo = multiArchivo
        self.nombreArchivo = nombreArchivo

    def insertar(self, escala, ruido, proximidad, capacidad, conteo, ciclos, tiempo, multiArchivo, nombreArchivo):
        self.escala = escala
        self.ruido = ruido
        self.proximidad = proximidad
        self.capacidad = capacidad
        self.conteo = conteo
        self.ciclos = ciclos
        self.tiempo = tiempo
        self.multiArchivo = multiArchivo
        self.nombreArchivo = nombreArchivo


def guardarReporte(reporte):
    fichero = file ( "paginas/static/paginaP/img/reporte.txt", "w" )
    nl = reporte
    pickle.dump ( nl, fichero )
    return nl


def cargarReporte():
    try:
        fichero = file ( "paginas/static/paginaP/img/reporte.txt" )
        r = pickle.load ( fichero )
        obj = Reporte ( r.escala, r.ruido, r.proximidad, r.capacidad, r.conteo, r.ciclos, r.tiempo, r.multiArchivo,
                        r.nombreArchivo )
        return obj
    except:
        n = Reporte ( 0.0, 0, 0.0, 0, 0, 0, 0.0, False, "Geo" )
        guardarReporte ( n )
        return n
