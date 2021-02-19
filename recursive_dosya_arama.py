import os
import sys

suanki_konum = os.getcwd()

istenen_hedef  = input("Aramak istediğiniz dosya adı : ").lower()
istenen_uzanti = input("Dosya uzantısı ?\nresim, video ya da ofis\n >>> ")

uzanti_liste = []

if istenen_uzanti == "resim":
    uzanti_liste = ['jpg','png','jpeg','bmp','gif','tiff']
elif istenen_uzanti == "video":
    uzanti_liste = ['avi','mp4','mkv','flv','wmv']
elif istenen_uzanti == "ofis":
    uzanti_liste = ['doc','docx','mpp','pptx','pst','ppsx','docx','pdf','xlsx','pps','xls','odt','txt']
else:
    uzanti_liste = []

say = 1
for kok_yol, alt_klasor, dosyalar in os.walk(suanki_konum):
    for dosya in dosyalar:
        dosyaKonumu = os.path.join(kok_yol, dosya)
        dosyaAdi, uzanti = dosya.split(".")[0], dosya.split(".")[-1]
        dosyaAdi = dosyaAdi.lower()
        uzanti   = uzanti.lower()

        if(len(uzanti_liste)!=0):
            # istenen uzantı dönen dosyaya uyuyorsa
            # ve dosya adları eşit ise
            # bulduk demektir
            if (uzanti in uzanti_liste) and (dosyaAdi==istenen_hedef):
                print('{}. '.format(say),end="")
                print('Adı : {} | yolu : {}'.format(dosyaAdi,dosyaKonumu))
                say += 1
        # uzantı yoksa dosya adı eşit olan tüm dosyalar yazdırılır
        else:
            if(istenen_hedef==dosyaAdi):
                print('{}. '.format(say),end="")
                print('Adı : {} | yolu : {}'.format(dosyaAdi,dosyaKonumu))
                say += 1