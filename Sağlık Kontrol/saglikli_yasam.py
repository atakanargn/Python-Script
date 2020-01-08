# Işletim sistemi ve dosya sistemi için kütüphane
import os
# Matematiksel işlemler için kütüphane
import math
# Zamanı öğrenmek için kütüphane
from datetime import datetime
# Bekletme işlemleri için sleep() fonksiyonu
from time import sleep

bugun = datetime.now()
tarih = bugun.strftime("%m/%d/%Y")

def bilgiler():
    # Veritabanı dosyasını açtık
    veritabani = open("veritabani.txt","r+")
    # İçeriğin her satırını diziye aktardık
    icerik     = veritabani.readlines()
    # Veritabanı dosyasını kapattık
    veritabani.close()
    # Ilk satırdaki kullanıcı bilgisi değişkenlerini çektik
    ad, yas, boy, kilo, kitleEndeks, kiloDurum, gunlukKalori = icerik[0].split("<:>")
    # Son satırdaki tarih, o tarihte alınan su ve alınan kalori miktarını çektik
    gun, su, kalori = icerik[len(icerik)-1].split("<:>")
    # Son gün, bugün değil ise yeni bir satıra yeni bir gün oluşturduk
    while(tarih!=gun):
        # Önceki gün su tüketimi 2000mL altındaysa, veriyi siler
        # yani önceki günü kaydetmemiş olur.
        if(int(su)<2000):
            icerik[len(icerik)-2] = icerik[len(icerik)-2][:-1]
            sonVeriSil = icerik.pop()
        # Yeni günü çektiğimiz içeriğin sonuna ekledik
        icerik.append(f"\n{tarih}<:>0<:>0")

        #Veritabanı dosyasına kaydettik
        veritabani = open("veritabani.txt","w")
        metin = ""
        for satir in icerik:
            metin += satir
        veritabani.write(metin)
        veritabani.close()

        # Tekrar kontrol ettik ve devam ettik
        veritabani = open("veritabani.txt","r+")
        icerik     = veritabani.readlines()
        gun, su, kalori = icerik[len(icerik)-1].split("<:>")
        veritabani.close()

    # Giriş yazısı
    print("=== SAĞLIKLI YAŞAM ===")
    print("= Hoşgeldin {}".format(ad))
    print("= Tarih : {}".format(gun))
    print("= Yaş   : {}".format(yas))
    print("= Boy   : {}cm | Kilo : {}kg".format(boy,kilo))
    print("= Durum : {}".format(kiloDurum))
    print("="*16)

    if gunlukKalori > kalori:
        print("= Günlük alman gereken kalori miktarını doldurmamışsın!")
        print("= Alman gereken kalori : {}".format(int(gunlukKalori)-int(kalori)))
    elif gunlukKalori < kalori:
        print("= Günlük alman gereken kalori miktarından fazlasını almışsın!")
        print("= Yakman gereken kalori : {}".format(int(kalori)-int(gunlukKalori)))
        print("= Kalori yakmanı sağlayacak faaliyetler şöyle listelenebilir:")
        print("= 1) -----------")
        print("= 2) -----------")
        print("= 3) -----------")
    else:
        print("= Günlük alman gereken kalori tam yerinde olmuş :)")
    print("="*16)

    if 2000 > int(su):
        print("= Günlük su tüketimini tamamlamamışsın!")
        print("= Su tüketimini tamamlamazsan, bugünkü verilerin kaydedilmeyecek!")
        print("= Alman gereken su miktarı : {}mL".format(2000-int(su)))
        print("= Bu da yaklaşık {} bardak su eder!".format(int((2000-int(su))/200)))
    else:
        print("= Tebrikler günlük su tüketimini tamamlamışsın.")
        print("= Fazlasını içmende bir sakınca yok :)")
    print("="*16)
    print("= Bilgileriniz listelendi.")
    print("= DEVAM ETMEK İÇİN")
    print("= ENTER TUŞUNA BASIN!")
    input("="*16)

def kaloriEkle():
    print("= Lütfen eklemek istediğin")
    print("= kalori miktarını gir")
    yeniKalori = int(input("=  >>> "))
    veritabani = open("veritabani.txt","r")
    icerik     = veritabani.readlines()
    veritabani.close()
    gun, su, kalori = icerik[len(icerik)-1].split("<:>")
    kalori = int(kalori)
    kalori += yeniKalori
    icerik[len(icerik)-1] = f"{gun}<:>{su}<:>{kalori}"

    veritabani = open("veritabani.txt","w")
    metin = ""
    for satir in icerik:
        metin += satir
    veritabani.write(metin)
    veritabani.close()
    print("Verileriniz kaydediliyor lütfen bekleyin!")
    sleep(3)

def suEkle():
    print("= Lütfen eklemek istediğin")
    print("= su miktarını gir(mL cinsinden)")
    yeniSu = int(input("=  >>> "))
    veritabani = open("veritabani.txt","r")
    icerik     = veritabani.readlines()
    veritabani.close()
    gun, su, kalori = icerik[len(icerik)-1].split("<:>")
    su = int(su)
    su += yeniSu
    icerik[len(icerik)-1] = f"{gun}<:>{su}<:>{kalori}"

    veritabani = open("veritabani.txt","w")
    metin = ""
    for satir in icerik:
        metin += satir
    veritabani.write(metin)
    veritabani.close()
    print("Verileriniz kaydediliyor lütfen bekleyin!")
    sleep(3)

def yeniKullanici():
    print("=== SAĞLIKLI YAŞAM ===")
    print("= Sağlıklı Yaşam programına hoşgeldin.")
    print("= Öncelikle adını öğrenebilir miyim ?")
    ad = input("=  >>> ")
    print("= Şimdi yaşını öğrenelim?")
    yas = input("=  >>> ")
    print("= Tebrikler {} ! Sağlıklı yaşam için".format(ad))
    print("= ilk adımını atmış bulunmaktasın.\n")
    print("=== VÜCUT KİTLE ENDEKSİ HESAPLAMA ===")
    print("= Boyun kaç santimetre?")
    boy = input("=  >>> ")
    print("= Kaç kilogramsın?")
    kilo = input("=  >>> ")
    # Kitle endeksi, endekse göre durum ve öneri mesajı
    kitleEndeks, kiloDurum, mesaj = kitleEndeksi(boy,kilo)
    kalori = yasKalori(yas)
    veritabani = open("veritabani.txt","w")
    veritabani.write(f"{ad}<:>{yas}<:>{boy}<:>{kilo}<:>{kitleEndeks}<:>{kiloDurum}<:>{kalori}\n{tarih}<:>0<:>0")
    veritabani.close()
    print("Verileriniz kaydediliyor lütfen bekleyin!")
    sleep(3)

def yasKalori(yas):
    yas = int(yas)
    if(yas>=9 and yas<=13):
        kalori = 1700
    elif(yas>=14 and yas<=30):
        kalori = 2200
    elif(yas>=31):
        kalori = 2000
    return kalori

def kitleEndeksi(boy,kilo):
    boy   = float(boy)/100
    kilo  = int(kilo)
    kitle = float(kilo / (boy**2))
    kitle = float("%0.1f"%(kitle))
    if(kitle>=0 and kitle<=18.4):
        durum = "ZAYIF"
        mesaj = "Boyunuza oranla ağırlığınız zayıf kategorisine giriyor. Bu da ideal kilonuza ulaşmak için kilo almanız gerektiği anlamındadır."
    elif(kitle>=18.5 and kitle<=24.9):
        durum = "NORMAL"
        mesaj = "En ideal kilonuzdasınız. Yeterli ve dengeli beslenmeye özen gösterirken sporu  da ihmal etmeyin."
    elif(kitle>=25 and kitle<=29.9):
        durum = "FAZLA KİLOLU"
        mesaj = "Kilonuz boyunuza oranla fazla. Fazla kilolarınızın tehlike arz etmesini istemiyorsanız acilen önlem almalısınız."
    elif(kitle>=30 and kitle<=34.9):
        durum = "ŞİŞMAN (1.SEVIYE OBEZ)"
        mesaj = "Vücudunuz boy oranınıza göre artık biraz daha tehlikeli bir durumda. Diğer bir deyimle şişman kategorisindesiniz. İdeal kiloya ulaşmak için bir diyetisyene başvurun"
    elif(kitle>=35 and kitle<=44.9):
        durum = "ŞİŞMAN (2.SEVIYE OBEZ)"
        mesaj = "İçinde bulunduğunuz kilo boyunuza oranla çok fazla ve şişmanlığın ikinci aşamasındasınız. Bu durum kalp ve damar rahatsızlıklarına yol açabilir."
    elif(kitle>=45):
        durum = "AŞIRI ŞİŞMAN (3.SEVIYE OBEZ)"
        mesaj = "Gözle de çok rahat görelebilecek bir şişmanlık, yine gözle görülen hastalıklara neden olacaktır. Bu nedenle bir an önce kilo vermelisiniz."

    return (kitle, durum, mesaj)

def oncekiGun():
    veritabani = open("veritabani.txt","r")
    icerik     = veritabani.readlines()
    veritabani.close()
    gun, su, kalori = icerik[len(icerik)-1].split("<:>")
    print((16*"=" + "\n= Tarih : {}\n= Kalori : {} | Su : {}mL\n" + "="*16).format(gun,su,kalori))
    input("Devam etmek için Enter'a bas!")
    
if os.path.isfile("veritabani.txt"):
    bilgiler()
else:
    yeniKullanici()

while True:
    print("=== MENU ===")
    print("= (1) - Bilgilerim")
    print("= (2) - Kalori Ekle")
    print("= (3) - Su Ekle")
    print("= (4) - Önceki günü getir")
    print("= (5) - Çıkış")
    print("= Yapmak istediğin işlemi seç")
    menuGetir = input("=  >>> ")
    if(menuGetir == "1"):
        bilgiler()
    elif(menuGetir == "2"):
        kaloriEkle()
    elif(menuGetir == "3"):
        suEkle()
    elif(menuGetir == "4"):
        oncekiGun()
    elif(menuGetir == "5"):
        break
    else:
        print("Geçersiz menü girişi!")
        input("Devam etmek için Enter'a bas!")