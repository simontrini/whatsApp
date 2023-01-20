from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
w, h = landscape(letter)
nombre = "Cruz Mery Villegas"
c = canvas.Canvas("certificado{0}.pdf".format(nombre.strip()), pagesize=landscape(letter))

c.drawImage("certificadoLuis.jpeg", 7, 7, w+12, h+12)
#c.rect(5, 5, w-10, h-10)
c.setFont("Times-Roman", 30)
c.drawString((w/2)-100, h-(h/2)-30, nombre)
c.setFont("Times-Roman", 20)
c.drawString((w/2)+30, h-(h/2)-75, "24/11/2022")
c.drawString((w/2)+30, h-(h/2)-95, "24 Horas")
c.setFont("Times-Roman", 14)
c.drawString((w/2)-80, 0, "Certificado Numero :241120221")
c.showPage()
c.save()