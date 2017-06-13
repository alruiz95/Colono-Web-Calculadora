from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.lib.utils import ImageReader
from PIL import Image
import PIL
from django.http import HttpResponse
import paginas.manejo.reporte as rep
from io import BytesIO
import os
import CONSTANTS
from reportlab.lib.units import cm

def saveFilePDF():
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

    fecha = datetime.now()
    fechaStr = str(fecha.day) + "/" + str(fecha.month) + "/" + str(fecha.year)

    reporte = rep.cargarReporte()
    c = canvas.Canvas(response, pagesize=A4)

    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 750, 'Reporte de resutados')

    c.setFont('Helvetica-Bold', 22)
    c.drawString(460, 750, fechaStr)

    c.setFont('Helvetica', 12)
    c.drawString(30, 710, "Escala pixel x metro:")
    c.drawString(150, 710, str(reporte.escala))
    c.drawString(30, 695, "Filtro de ruido:")
    c.drawString(150, 695, str(reporte.ruido))
    c.drawString(30, 680, "Proximidad:")
    c.drawString(150, 680, str(reporte.proximidad))
    c.drawString(30, 665, "Duracion de proceso:")
    c.drawString(150, 665, str(reporte.tiempo))

    c.drawString(30, 615, "Nombre del Archivo:")
    c.drawString(150, 615, str(reporte.nombreArchivo))
    c.drawString(30, 600, "Conteo de pinnas:")
    c.drawString(150, 600, str(reporte.conteo))

    tamImage = os.stat(CONSTANTS.JPG_FULL_DIR).st_size
    Image.MAX_IMAGE_PIXELS = tamImage + 100

    jpgfile = ImageReader(CONSTANTS.JPG_FULL_DIR)
    c.drawImage(jpgfile, 30, 20,  width=19*cm, preserveAspectRatio=True)

    c.showPage()
    c.save()
    return response