from pushetta import Pushetta
from bs4 import BeautifulSoup
import requests

API_KEY="PUSHETTA-API-KEY-HERE"
bildirim=Pushetta(API_KEY)
#p.pushMessage("Anime Bildirim", "Python Deneme!")

r = requests.get('https://www.dizimob1.com/')
source = BeautifulSoup(r.content, "html.parser")
A = source.findAll("div", attrs={"class", "listfilm"})

content=""
for element in A:
    content+=str(element)

source = BeautifulSoup(content, "html.parser")

animeDosya=open("animeler.txt","r")
animeler = animeDosya.readlines()
animeDosya.close()
animeAd    = []
animeBolum = []
for anime in animeler:
    nAnime = anime.split('<:>')
    animeAd.append(nAnime[0].strip())
    animeBolum.append(nAnime[1].strip())

A = source.findAll("a")
say=-1
for element in A:
    say+=1
    for anime in animeAd:
        if(element.text==anime):
            guncelBolum = A[say+1].text.strip()[:-7]
            guncelBolum = guncelBolum[-3:]
            guncelBolum = guncelBolum.strip()
            if(not(guncelBolum<=animeBolum[animeAd.index(anime)]) ):
                bildirim.pushMessage("Anime Bildirim",anime+" animesinin yeni bölümü gelmiş!\n"+guncelBolum+".Bölüm!")
                animeBolum[animeAd.index(anime)]=guncelBolum

animeDosya = open("animeler.txt","w")
for anime in animeAd:
    animeDosya.write(anime+"<:>"+animeBolum[animeAd.index(anime)]+"\n")
animeDosya.close()
