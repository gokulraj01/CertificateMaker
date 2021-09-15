import os
from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Page Properties (Defaults to Landscape A4)
pageWidth = 29.7
pageHeight = 21
opFolder = "Output"     # Output Folder Path
bgFile = "cert2.webp"   # Background Image Path
fontName = "OCRAEXT"    # Font Filename to Use
nameY = 200             # Vertical Position of Name from Bottom Edge in pt
pageWidthPt = pageWidth*72/2.54
pageHeightPt = pageHeight*72/2.54

class CertGen:
    def initPage(width: float, height: float, bg_path: str, name_Y: float):
        global pageHeight, pageWidth, bgFile, pageHeightPt, pageWidthPt, nameY
        pageWidth = width
        pageHeight = height
        bgFile = bg_path
        pageWidthPt = pageWidth*72/2.54
        pageHeightPt = pageHeight*72/2.54
        nameY = name_Y

    def makeCertificate(title, filename, std_name, y):
        print("Generating Certificate for %s"%std_name)
        # Initialize PDF Properties and Assets
        bgImg = Image.open(bgFile)
        bgImg = bgImg.resize((int(pageWidthPt), int(pageHeightPt)))
        Image.Image.save(bgImg, './assets/temp_cert_bg.bmp')
        pdfmetrics.registerFont(TTFont(fontName, "%s.ttf"%fontName))

        # Make Certificate
        canvas = Canvas("./%s/%s.pdf"%(opFolder, filename), pagesize=(pageWidthPt, pageHeightPt))
        canvas.setTitle(title)
        canvas.drawImage('./assets/temp_cert_bg.bmp', 0, 0)
        canvas.setFont(fontName, 30)
        canvas.drawCentredString(pageWidthPt/2, y, std_name)
        canvas.save()

    def initOpFolder(fold_name: str):
        try:
            global opFolder
            opFolder = fold_name
            os.mkdir(fold_name)
        except FileExistsError:
            print("Folder Already Exists!!")