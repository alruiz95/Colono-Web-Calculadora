from paginas.manejo.conexion import BDConexion
import CONSTANTS
import geoReferencia
import os
import sys
from PIL import Image
from PIL import ImageDraw
import cv2


def crearImgenResultados():
    if (convertImage()):
        print "==========================> ", len(CONSTANTS.LISTAPUNTOS)
        print "==========================> ", CONSTANTS.LISTAPUNTOS

        listaPuntosNu = []
        print CONSTANTS.GEOREFERENCIA.geoT
        for elemento in CONSTANTS.LISTAPUNTOS:
            x,y = GeocoordToPixelCoord(elemento[0],elemento[1])
            listaPuntosNu.append([x,y])
        print "==========================> ", listaPuntosNu

        tamImage = os.stat(CONSTANTS.JPG_FULL_DIR).st_size
        Image.MAX_IMAGE_PIXELS = tamImage + 100
        jpgfile = Image.open(CONSTANTS.JPG_FULL_DIR)

        draw = ImageDraw.Draw(jpgfile)
        for elemento in listaPuntosNu:
            draw.ellipse((drawPos(elemento[0],elemento[1],8)), fill='red', outline='blue')



        jpgfile.save(CONSTANTS.JPG_FULL_DIR)
        del draw
        del jpgfile
        return True

    return False


def convertImage():
    if (CONSTANTS.TIFF_DIR==''):
        return False
    os.system (
        "gdal_translate -of GTiff " + CONSTANTS.TIFF_DIR + ' '+CONSTANTS.JPG_FULL_DIR)
    return True


def GeocoordToPixelCoord( px, py):
    s = px - CONSTANTS.GEOREFERENCIA.geoT[0]
    t = py - CONSTANTS.GEOREFERENCIA.geoT[3]
    det = CONSTANTS.GEOREFERENCIA.geoT[1] * CONSTANTS.GEOREFERENCIA.geoT[5] - CONSTANTS.GEOREFERENCIA.geoT[2] * CONSTANTS.GEOREFERENCIA.geoT[4]
    x = (s * CONSTANTS.GEOREFERENCIA.geoT[5] - CONSTANTS.GEOREFERENCIA.geoT[2] * t) / det
    y = (t * CONSTANTS.GEOREFERENCIA.geoT[1] - CONSTANTS.GEOREFERENCIA.geoT[4] * s) / det
    return int ( x ), int ( y )

def drawPos (x,y,diametro):
    return x-diametro,y-diametro,x+diametro,y+diametro