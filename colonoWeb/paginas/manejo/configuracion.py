import pickle


class Configuracion:
    def __init__(self, escala, ruido, proximidad, capacidad,multiArchivo, nombreArchivo):
        self.escala = escala
        self.ruido = ruido
        self.proximidad = proximidad
        self.capacidad = capacidad
        self.multiArchivo=multiArchivo
        self.nombreArchivo=nombreArchivo

    def datosString(self):
        return "Escala: " + str ( self.escala ) + " Ruido: " + str ( self.ruido ) + " Proximidad: " + str (
            self.proximidad ) + " Capacidad Memoria: " + str ( self.capacidad +" MultiArchivo: "+str(self.multiArchivo)
                                                               +" Nombre del Archivo: "+str(self.nombreArchivo))


def cargar():
    try:
        fichero = file ( 'paginas\static\paginaP\conf\configuracion.txt' )
        r = pickle.load ( fichero )
        obj = Configuracion ( r.escala, r.ruido, r.proximidad, r.capacidad, r.multiArchivo, r.nombreArchivo )
        return obj
    except:
        guardar ( 0.3, 6, 54.5, 50000000, False, "Geo" )
        return Configuracion ( 0.3, 6, 54.5, 50000000, False, "Geo" )


def guardar(escala, ruido, proximidad, capacidad, multiArchivo,nombreArchivo):
    fichero = file ( 'paginas\static\paginaP\conf\configuracion.txt', 'w' )
    nl = Configuracion ( escala, ruido, proximidad, capacidad, multiArchivo, nombreArchivo )
    pickle.dump ( nl, fichero )
    return nl


def predeterminado():
    return guardar ( 0.3, 6, 54.5, 50000000, False, "Geo" )
