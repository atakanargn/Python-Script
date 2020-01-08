# stem    : kök anlamına gelir
# stemmer : kök ayırıcı/bulucu anlamındadır
from snowballstemmer import stemmer

# Türkçe, Doğal dil işleme kütüphanesi
# Şuanki Python seviyem ile Doğal dil işleme yapamadığımdan bu kütüphaneyi seçtim
import turkishnlp

obj = turkishnlp.detector.TurkishNLP()
print("Türkçe kelime seti indiriliyor!")
obj.download()
print("Türkçe kelime seti ayarlanıyor.")
obj.create_word_set()

# Kelime veya Cümle içindeki kelimelerin köklerini ayırabilir
# Ancak Doğal dil işleme kullanmadığımızdan
#   %60-70 oranlarında doğru çalışacaktır
def kokBulucu(kelimeKumesi):
    kokBulucu = stemmer('turkish')
    kelimeKumesi = kelimeKumesi.lower()
    return ("Kökler : {}".format(kokBulucu.stemWords(kelimeKumesi.split())))

# Girilen cümle Türkçe mi kontrol etmek için
# yazdığımız fonksiyon
def cumleTurkceMi(cumle):
    turkcemi = obj.is_turkish(cumle)
    if turkcemi:
        return ("Girilen cümle Türkçedir.")
    else:
        return ("Girilen cümle Türkçe değil.")

# Girilen kelime Türkçe mi kontrol etmek için
# yazdığımız fonksiyon
def kelimeTurkceMi(kelime):
    turkcemi = obj.is_turkish_origin(kelime)
    if turkcemi:
        return ("{} kelimesi Türkçe kökenlidir.".format(kelime))
    else:
        return ("{} kelimesi Türkçe kökenli değildir.".format(kelime))

# Program sürekli çalışmalı
# bu yüzden sonsuz döngüye aldık
while 1:
    # Menü yazdırdık ve kullanıcıdan seçim istedik
    print("1. Kelime veya Cümleyi köklerine ayır")
    print("2. 'Cümle Türkçe mi?' test et")
    print("3. 'Kelime Türkçe mi?' test et")
    print("4. Çıkış")
    menu = input("IŞLEM = ")

    if menu == "1":
        # Kök bulma işlemi
        # Kullanıcıdan kelime veya cümleyi girmesini istedik
        kelimeKumesi = input("Kelime veya Cümleyi girin\n ::: ")
        # Yukarıda yazdığımız fonksiyon yardımıyla
        # Köklerine ayırıp, ayir değişkenine atadık
        ayir = kokBulucu(kelimeKumesi)
        # Aldığımız değerleri ekrana yazdırdık
        print(ayir)
        input("Devam etmek için Enter'a basınız!")
    elif menu == "2":
        # Cümle Türkçe mi değil mi tanıma işlemi
        # Kullanıcıdan cümleyi girmesini istedik
        cumle    = input("Cümleyi girin\n ::: ")
        # Yukarıdaki fonksiyondan sonuç döndürdük
        # ve turkceMi değişkenine atadık
        turkceMi = cumleTurkceMi(cumle)
        # Gelen değeri ekrana yazdırdık
        print(turkceMi)
        input("Devam etmek için Enter'a basınız!")
    elif menu == "3":
        # Kelime Türkçe mi değil mi tanıma işlemi
        # Kullanıcıdan kelimeyi girmesini istedik
        kelime    = input("Kelimeyi girin\n ::: ")
        # Yukarıdaki fonksiyondan sonuç döndürdük
        # ve turkceMi değişkenine atadık
        turkceMi = kelimeTurkceMi(kelime)
        # Gelen değeri ekrana yazdırdık
        print(turkceMi)
        input("Devam etmek için Enter'a basınız!")
    elif menu == "4":
        break
    else:
        print("Geçersiz menü değeri girdiniz.")
        input("Devam etmek için Enter'a basınız!")