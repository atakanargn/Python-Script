def ogrenciEkle():
    veritabani = open("./veri.txt","r")
    ogrenciler = veritabani.readlines()
    veritabani.close()

    print("# Öğrenci; ")
    ad     = input("# Adı       : ")
    soyad  = input("# Soyadı    : ")
    tcNo  = input("# TC Kimlik : ")
    while len(tcNo)!=11:
        print("# TC Kimlik numarası 11 haneli olmalıdır.")
        tcNo   = input("# TC Kimlik : ")
    okulno = len(ogrenciler)+1
    print("# Okul numarası : "+str(okulno))

    for ogrenci in ogrenciler:
        ad,soyad,tc,okulno = ogrenci.split(",")
        okulno = okulno[:-1]
        if(tc==tcNo):
            print("# Bu kimlik numarasına sahip biri kayıtlı!")
            veritabani.close()
            return
        else:
            ogrenciler.append("{},{},{},{}\n".format(ad,soyad,tcNo,okulno))
            break

    metin = ""
    for satir in ogrenciler:
        metin += satir
    
    veritabani = open("./veri.txt","w")
    veritabani.write(metin)
    veritabani.close()

    print("# Öğrenci eklendi.")

def ogrenciSil():
    veritabani = open("./veri.txt","r")
    ogrenciler = veritabani.readlines()
    veritabani.close()

    tcNo  = input("# TC Kimlik : ")
    while len(tcNo)!=11:
        print("# TC Kimlik numarası 11 haneli olmalıdır.")
        tcNo   = input("# TC Kimlik : ")

    for ogrenci in ogrenciler:
        ad,soyad,tc,okulno = ogrenci.split(",")
        if(tc==tcNo):
            ogrenciler.remove(ogrenci)
    
    metin = ""
    for satir in ogrenciler:
        metin += satir
    
    veritabani = open("./veri.txt","w")
    veritabani.write(metin)
    veritabani.close()

    print("# Öğrenci silindi.")

def ogrenciGuncelle():
    print("### Öğrenci Güncelleme ###\n#")
    veritabani = open("./veri.txt","r")
    ogrenciler = veritabani.readlines()
    veritabani.close()

    tcNo  = input("# TC Kimlik : ")
    while len(tcNo)!=11:
        print("# TC Kimlik numarası 11 haneli olmalıdır.")
        tcNo   = input("# TC Kimlik : ")
    print("#\n# Yeni Bilgiler;")
    yAd     = input("# Ad        : ")
    ySoyad  = input("# Soyad     : ")
    yTcNo   = input("# TC Kimlik : ")
    while len(yTcNo)!=11:
        print("# TC Kimlik numarası 11 haneli olmalıdır.")
        yTcNo   = input("# TC Kimlik : ")
    yOkulno = input("# Okul no   : ")

    for ogrenci in ogrenciler:
        ad,soyad,tc,okulno = ogrenci.split(",")
        okulno = okulno[:-1]
        if(tc==tcNo):
            ogrenciler[ogrenciler.index(ogrenci)] = ("{},{},{},{}\n".format(yAd,ySoyad,yTcNo,yOkulno))
    
    metin = ""
    for satir in ogrenciler:
        metin += satir
    
    veritabani = open("./veri.txt","w")
    veritabani.write(metin)
    veritabani.close()

    print("# Öğrenci güncellendi.")

def ogrenciListele():
    print("### Öğrenci Listeleme ###\n#")

    veritabani = open("./veri.txt","r")
    ogrenciler = veritabani.readlines()
    veritabani.close()

    for ogrenci in ogrenciler:
        ad,soyad,tc,okulno = ogrenci.split(",")
        okulno = okulno[:-1]
        print("#"*16)
        print("# Ad        : "+str(ad))
        print("# Soyad     : "+str(soyad))
        print("# TC Kimlik : "+str(tc))
        print("#"*16+("\n#"))
    input("## DEVAM ETMEK İÇİN ENTER ##")

while True:
    print("### ÖĞRENCİ OTOMASYONU ###")
    print("# 1) Öğrenci Ekle")
    print("# 2) Öğrenci Güncelle")
    print("# 3) Öğrenci Sil")
    print("# 4) Öğrenci Listele")
    print("# 5) Çıkış")
    menu = input("# Işlem seçin : ")
    if(menu   == "1"):
        ogrenciEkle()
    elif(menu == "2"):
        ogrenciGuncelle()
    elif(menu == "3"):
        ogrenciSil()
    elif(menu == "4"):
        ogrenciListele()
    elif(menu == "5"):
        break
    else:
        print("## GEÇERSİZ GİRİŞ YAPILMIŞ ##")