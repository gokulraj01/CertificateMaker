import certgen

names = ["Katlyn Mosby","Tenesha Wells","Yuri Somerville","Jose Scroggins"]

clgname = "Certificate Generator College"
fontsize = 25
fnormal = "LHANDW"
fbold = "CORBEL"

cert = certgen.CertGen("sample")
cert.initPage(29.7, 21, "./assets/Cert.jpeg")
cert.initSerial("2021/CGEN/TST", 700, 25)

for name in names:
    cert.drawCenString(name, fontsize, 480, 305, fnormal)
    cert.drawCenString(clgname, fontsize-5, 485, 255, fbold)
    print(f"Generating Certificate: {name}")
    cert.makeCertificate("MyCert", name, [name, clgname])

cert.makeCSVReport("report")
cert.makeJSONReport("report")