from bs4 import BeautifulSoup
import requests
from random import randint
import sys
"""
SDGASDGH
SADH
ASH
SDH
SAHSA
HSH

"""
# Çektiğimiz içeriğin türünü çekiyoruz (Film veya Dizi)
def turCek():
    tur = None
    # Çektiğimiz sayfa film veya dizi sayfası değilse, tekrar tekrar sayfayı çekiyoruz
    while (str(type(tur)) == "<class 'NoneType'>"):
        # Rastgele sayı ürettik
        rastgele = randint(1,2000000)
        # Sayıyı String'e çevirdik
        rastgele = str(rastgele)
        # Sayı değeri 7 haneli değilse, başına sıfırlar ekleyerek 7 haneli olmasını sağladık
        while len(rastgele) < 7:
            rastgele = "0" + rastgele
        # Geçerli link oluşturduk
        link = "https://www.imdb.com/title/tt" + rastgele
        # Sayfayı komple çektik
        try:
            istek = requests.get(link)
        except:
            print("INTERNET YOK!")
            sys.exit(0)
        # Sayfa kaynağını kütüphane ile parse ettik
        kaynak = BeautifulSoup(istek.content, "html.parser")
        # Sayfa içinden türün bulunduğu kısmı çektik
        tur = kaynak.find("script", attrs={"type":"application/ld+json"})
    # Tür olan kısmı temizleyip, "@type" yazan kısım içinden "Movie" veya "TVEpisode" değerini aldık
    tur = tur.text.split("\n")[2].strip()
    tur = tur.replace('"',"")
    tur = tur.replace("@type: ","")[:-1]
    
    # Tür ve sayfa Kaynağını döndürdük
    return {"tur":tur, "kaynak":kaynak}

# Tür ve sayfa Kaynağını aldık
site = turCek()

# Tür "Movie" olana kadar yeni film çektirdik
while site["tur"] != "Movie":
    site = turCek()

# Tür "Movie" yani Film ise kaynağını çektik
kaynak = site["kaynak"]

# Film başlık
# <div class="title_wrapper"></div> içeriğini çektik
filmUstBilgi = kaynak.find("div", attrs={"class":"title_wrapper"})
filmUstBilgi = BeautifulSoup(str(filmUstBilgi), "html.parser")

# Çektiğimiz içerik içinden <h1></h1> içeriğinden film adını aldık
filmBaslik = filmUstBilgi.find("h1").text[0:-8]

# film adı uzunluğu
baslikUzunluk = len(filmBaslik)

# Film yılını aldık
filmYil = filmUstBilgi.find("h1").text
filmYil = filmYil.strip()
filmYil = filmYil[baslikUzunluk+1:baslikUzunluk+7]

# Film puanını aldık
filmPuan = kaynak.find("div",attrs={"class":"ratingValue"})

# Sitede film puanı girilmemişse, (Puanı yok!) yazdırdık
if(str(type(filmPuan))=="<class 'NoneType'>"):
    filmPuan = "(Puanı Yok!)"
else:
    filmPuan = filmPuan.text.strip()

# Film konusunu çektik
filmKonu = kaynak.find("div",attrs={"class":"summary_text"})
filmKonu = filmKonu.text.strip()
# Film konusu yazılmamışsa, "Filmin konusu yazılmamış." yazdırdık
if("Add a Plot" in filmKonu):
    filmKonu = "Filmin konusu yazılmamış."

# Çektiğimiz değerleri ekrana bastık
print("=== RASTGELE FİLM ÖNERİNİZ ===")
print("= Film adı : "+filmBaslik)
print("= Film yılı :"+filmYil)
print("= Film puanı : "+filmPuan)
print("= Film konusu : \n    "+filmKonu)
print("="*30)