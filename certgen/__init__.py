import os
from PIL import Image
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class CertGen:
    # Page Properties (Defaults to Landscape A4)
    pageWidth = 29.7
    pageHeight = 21
    opFolder = "Output"     # Output Folder Path
    bgFile = "cert2.webp"   # Background Image Path
    # serialFontName = "LUCON"    # Font Filename to Use for numbering
    nameY = 200             # Vertical Position of Name from Bottom Edge in pt
    pageWidthPt = pageWidth*72/2.54
    pageHeightPt = pageHeight*72/2.54
    fields = []
    serial = {'status': False}
    report = []

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
    
    def initSerial(self, prefix: str, x_offset: int, y: int, font:str="LUCON"):
        pdfmetrics.registerFont(TTFont(font, f"{font}.ttf"))
        self.serial = {
            'font': font,
            'status': True,
            'pref': prefix,
            'n': 1,
            'x': x_offset,
            'y': y
        }

    def drawSlNo(self, can: Canvas, uid1: str, uid2: str):
        can.setFont(self.serial['font'], 12)
        num = "%s%03d"%(self.serial['pref'], self.serial['n'])
        can.drawCentredString(self.serial['x'], self.serial['y'], f"CertNo: {num}")
        self.report.append([uid1, uid2, num])
        self.serial['n'] += 1

    def makeCertificate(self, title: str, filename: str, uid1: str, uid2:str="n/a"):
        # Initialize PDF Properties and Assets
        bgImg = Image.open(self.bgFile)
        # bgImg = bgImg.resize((int(self.pageWidthPt), int(self.pageHeightPt)), resample=Image.LANCZOS)
        Image.Image.save(bgImg, './assets/temp_cert_bg.bmp')

        # Make Certificate
        canvas = Canvas("./%s/%s.pdf"%(self.opFolder, filename), pagesize=(self.pageWidthPt, self.pageHeightPt))
        canvas.setTitle(title)
        canvas.drawImage('./assets/temp_cert_bg.bmp', 0, 0, self.pageWidthPt, self.pageHeightPt)
        for f in self.fields:
            pdfmetrics.registerFont(TTFont(f['fname'], f"{f['fname']}.ttf"))
            canvas.setFont(f['fname'], f['size'])
            canvas.drawCentredString(f['x'], f['y'], f['data'])
        if(self.serial['status']):
            self.drawSlNo(canvas, uid1, uid2)
        canvas.save()
        self.fields = []
    
    def makeReport(self, filename: str):
        print(f"Generating report to {filename}.csv")
        f = open(f"{self.opFolder}/{filename}.csv", 'w+')
        f.write("Data0, Data1, CertNo\n")
        for entry in self.report:
            f.write(f"{entry[0]}, {entry[1]}, {entry[2]}\n")
        f.close()
