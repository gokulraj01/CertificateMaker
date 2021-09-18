from reportlab.pdfbase.pdfmetrics import FontError
import certgen

cert = certgen.CertGen("CertOP")
cert.initPage(29.7, 21, "./assets/Cert.jpeg")

name = "Manoj Thankappan"
clgname = "Sree Chithra Thirunal College of Engineering"
fontsize = 25
fnormal = "LHANDW"
fbold = "corbel"


cert.drawCenString(name, fontsize, 480, 305, fnormal)
cert.drawCenString(clgname, fontsize-5, 485, 255, fbold)
print(f"Generating Certificate: {name}")
cert.makeCertificate("MyCert", "manoj")