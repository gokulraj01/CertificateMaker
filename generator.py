import certgen

cert = certgen.CertGen

cert.initOpFolder("CetOP")
cert.initPage(29.7, 21, "assets/cert2.webp", 100)

names = ["Francine Prentice","Porfirio Seawell","Pat Rosol","Reynaldo Forcier","Andrew Kos","Myrna Fredrickson","Lura Stec","Madlyn Mantooth","Lemuel Arterburn","Sydney Chery","Huong Rehm","Reba Rodgers","Karole Lucy","Shonna Begin","Leana Ishikawa","Celestina Chisum","Zena Coolbaugh","Le Stickel","Christine Saling","Claudie Bellone"]

name = names[1]
cert.makeCertificate("Lets C | %s"%name, name, name, 200)
