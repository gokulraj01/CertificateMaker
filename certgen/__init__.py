import os
from PIL import Image
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class CertGen:
    # Page Properties (Defaults to Landscape A4)
    pageWidth = 29.7
    pageHeight = 21
    opFolder = "Output"     # Output Folder Path
    bgFile = "cert2.webp"   # Background Image Path
    # fontName = "OCRAEXT"    # Font Filename to Use
    nameY = 200             # Vertical Position of Name from Bottom Edge in pt
    pageWidthPt = pageWidth*72/2.54
    pageHeightPt = pageHeight*72/2.54
    fields = []

    def __init__(self, fold_name: str):
        self.opFolder = fold_name
        try:
            os.mkdir(fold_name)
        except FileExistsError:
            print("Folder Already Exists!!")

    def initPage(self, width: float, height: float, bg_path: str):
        # global pageHeight, pageWidth, bgFile, pageHeightPt, pageWidthPt, nameY
        self.pageWidth = width
        self.pageHeight = height
        self.bgFile = bg_path
        self.pageWidthPt = self.pageWidth*72/2.54
        self.pageHeightPt = self.pageHeight*72/2.54

    def drawCenString(self, data: str, size: int, x_offset: int, y: int, font_name: str):
        obj = {}
        obj['data'] = data
        obj['x'] = x_offset
        obj['y'] = y
        obj['size'] = size
        obj['fname'] = font_name
        self.fields.append(obj)


    def makeCertificate(self, title, filename):
        # Initialize PDF Properties and Assets
        bgImg = Image.open(self.bgFile)
        bgImg = bgImg.resize((int(self.pageWidthPt), int(self.pageHeightPt)))
        Image.Image.save(bgImg, './assets/temp_cert_bg.bmp')

        # Make Certificate
        canvas = Canvas("./%s/%s.pdf"%(self.opFolder, filename), pagesize=(self.pageWidthPt, self.pageHeightPt))
        canvas.setTitle(title)
        canvas.drawImage('./assets/temp_cert_bg.bmp', 0, 0)
        for f in self.fields:
            pdfmetrics.registerFont(TTFont(f['fname'], f"{f['fname']}.ttf"))
            canvas.setFont(f['fname'], f['size'])
            canvas.drawCentredString(f['x'], f['y'], f['data'])
        canvas.save()