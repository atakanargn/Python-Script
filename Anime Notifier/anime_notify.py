# Kütüphaneleri import ettik
from pushetta import Pushetta
from bs4 import BeautifulSoup
import requests
from os import getcwd

# Pushetta için ApiKey'imizi buraya yazıyoruz
API_KEY="API-KEY-HERE"
kanal="Anime Bildirim"
# bildirim göndermek için Pushetta nesnesi oluşturduk
bildirim=Pushetta(API_KEY)
# Örnek kullanım
# bildirim.pushMessage("KanalAdı", "Bildirim")

# dizimob anasayfası kaynak kodunu çektik
r = requests.get('https://www.dizimob1.com/')
# BeautifulSoup ile kaynak kodu, html.parser modunda inceleyeceğiz
source = BeautifulSoup(r.content, "html.parser")
# A değişkeni bize class'ında listfilm bulunan tüm div leri çekti,
# sitede bu div ler dizi ve animelerin listelendiği divlerdir.
# yani tüm dizi ve animeleri çektik.
A = source.findAll("div", attrs={"class", "listfilm"})

# hata almamak için çektiklerimizi kaynak koda atıyoruz
content=""
for element in A:
    content+=str(element)
# Çektiklerimiz üstünden devam edelim
source = BeautifulSoup(content, "html.parser")

# animeler.txt okuma modunda dosyasını açtık
animeDosya=open(str(getcwd())+"/animeler.txt","r")
# tüm satırları diziye atadık
animeler = animeDosya.readlines()
# ve dosyayı runtime hataları almamak için kapattık.
animeDosya.close()
animeAd    = []
animeBolum = []
# Ben dosya içinde anime isimleri ve bölüm numaralarını "<:>" işareti ile ayırdım
# ayırdıklarımı animeAd ve animeBolum dizilerine aynı index numarasıyla atadık.
for anime in animeler:
    nAnime = anime.split('<:>')
    animeAd.append(nAnime[0].strip())
    animeBolum.append(nAnime[1].strip())

# Çektiğimiz div ler içinde daha fazla eleme yapmamız gerek
# bu yüzden sadece linkleri çektik
A = source.findAll("a")
say=-1
# Çektiğimiz tüm linkleri iterasyona aldık
for element in A:
    # index numarası saydırıyoruz
    say+=1
    # animeler.txt içinden aldığımız anime adlarınıda iterasyona aldık
    for anime in animeAd:
        # Eğer link içeriği, bizim listemizdeki animeyle aynıysa
        if(element.text==anime):
            # hemen sonraki linki al ve guncelBolum değişkenine ata
            # bi sonraki link bölümün adının geçtiği linktir
            # "3.Sezon  34. Bölüm" << bunun gibi bir String bunu işleme sokup sadece 34 sayısını almalıyız
            # ". Bölüm" 7 karakter o yüzden, en sondan 7 karakter hariç bi daha atamalıyız [:-7] ile
            guncelBolum = A[say+1].text.strip()[:-7]
            # "3.Sezon  34" kaldı, bunuda sondan sadece 4 karakter alalım
            guncelBolum = guncelBolum[-4:]
            # Içinde harf veya karakter varsa temizleyelim
            alfabe = ['a','b','c','d','e','f','g',
                      'h','i','j','k','l','m','n','o','p','r',
                      's','t','u','v','y','z','x','q','w','.',
                      ',',';',':','-','/','*','+']
            guncelBolum = guncelBolum.lower()
            for harf in alfabe:
                if harf in guncelBolum:
                    guncelBolum=guncelBolum.replace(harf," ")
            # Boşlukları temizleyelim
            guncelBolum = guncelBolum.strip()
            # Eğer guncelBolum, animeler.txt içindeki dosyaya eşit veya küçük değilse yani sadece büyükse
            if(not(guncelBolum<=animeBolum[animeAd.index(anime)]) ):
                # Anime adı ve bölüm sayısını, belirlenen kanala bildirim olarak gönder
                bildirim.pushMessage("Anime Bildirim",anime+" animesinin yeni bölümü gelmiş!\n"+guncelBolum+".Bölüm!")
                # Bölümler dizisindeki değeri güncelle
                animeBolum[animeAd.index(anime)]=guncelBolum
# animeler.txt aç
# Yeni değerlerle, baştan yaz
animeDosya = open(str(getcwd())+"/animeler.txt","w")
for anime in animeAd:
    animeDosya.write(anime+"<:>"+animeBolum[animeAd.index(anime)]+"\n")
animeDosya.close()
