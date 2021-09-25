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

    def drawSlNo(self, can: Canvas, uid: list):
        can.setFont(self.serial['font'], 12)
        num = "%s%03d"%(self.serial['pref'], self.serial['n'])
        can.drawCentredString(self.serial['x'], self.serial['y'], f"CertNo: {num}")
        uid.append(num)
        self.report.append(uid)
        self.serial['n'] += 1

    def makeCertificate(self, title: str, filename: str, uid: list):
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
            self.drawSlNo(canvas, uid)
        canvas.save()
        self.fields = []
    
    def makeCSVReport(self, filename: str):
        print(f"Generating report to {filename}.csv")
        f = open(f"{self.opFolder}/{filename}.csv", 'w+')
        data_i = len(self.report[0])
        header = ""
        for i in range(data_i-1):
            header += f"Data{i}, "
        header += "CertNo\n"
        f.write(header)
        for entry in self.report:
            op_str = ""
            for e in entry:
                op_str += f"{e}, "
            f.write(f"{op_str[:-2]}\n")
        f.close()
    
    def makeJSONReport(self, filename: str):
        spacing = 3
        spacer = " "
        print(f"Generating report to {filename}.json")
        f = open(f"{self.opFolder}/{filename}.json", 'w+')
        f.write("{\n\"report_data\": [\n")
        for entry in self.report:
            op_str = ""
            for e in entry:
                op_str += f"\"{e}\", "
            f.write(f"{spacer*spacing}[{op_str[:-2]}],\n")
        f.seek(f.tell()-3)
        f.write("\n]\n}")
        f.close()
