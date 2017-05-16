from paginas.manejo.conexion import BDConexion
import CONSTANTS
import geoReferencia
import os
import sys
from PIL import Image
from PIL import ImageDraw


def crearImgenResultados():
    if (convertImage()):
        jpgfile = Image.open(CONSTANTS.JPG_FULL_DIR)
        for elemento in CONSTANTS.LISTAPUNTOS:
            x,y = GeocoordToPixelCoord(elemento[0],elemento[1])
            draw = ImageDraw.Draw(jpgfile)
            draw.ellipse((x, y, 10, 10), fill=128)
            del draw

        jpgfile.save(CONSTANTS.JPG_FULL_DIR)
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
    s = px - self.geoT[0]
    t = py - self.geoT[3]
    det = self.geoT[1] * self.geoT[5] - self.geoT[2] * self.geoT[4]
    x = (s * self.geoT[5] - self.geoT[2] * t) / det
    y = (t * self.geoT[1] - self.geoT[4] * s) / det
    return int ( x ), int ( y )