#!/usr/bin/python3
#-*-coding:utf-8-*-

import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

def mailleriCek(excel,baslangic,bitis):
    # Mailler için boş dizi
    mailListe = []

    # Excel dosyasını açma
    mailDosya = openpyxl.load_workbook(excel);
    # Excel dosyası
    mailler=mailDosya.active

    # Excel dosyası A sutünunu
    # istenilen adet kadar çekme
    for i in range(baslangic,bitis,1):
        alici=mailler['A'+str(i)]
        mailListe.append(alici.value)
    return mailListe

def gonder(alicilar,konu,icerik,resim,mail,sifre):
    sunucu = smtplib.SMTP('smtp.gmail.com', 587)
    sunucu.starttls()
    sunucu.login(mail,sifre)

    mesaj = MIMEMultipart()
    mesaj['From'] = mail
    mesaj['To'] = ";".join(alicilar)
    mesaj['Subject'] = konu
    mesaj.attach(MIMEText(icerik, 'plain'))

    if(isinstance(resim,list)):
        for img in resim:
            imajUrl = open(img, 'rb').read()
            imaj = MIMEImage(imajUrl, name=os.path.basename(img))
            mesaj.attach(imaj)
    else:
        imajUrl = open(resim, 'rb').read()
        imaj=MIMEImage(imajUrl, name=os.path.basename(resim))
        mesaj.attach(imaj)
    metin=mesaj.as_string()

    try:
        sunucu.sendmail(mail,alicilar,metin)
        sunucu.quit()
        print("MAIL GONDERILDI.")
    except EOFError:
        sunucu.quit()
        print("HATA")

#Maillerin olduğu dizi

#maillerim = mailleriCek("MailListe.xlsx", başlangıç, bitiş)
maillerim = mailleriCek("MailListe.xlsx",1,1000) 
#Gönderilecek mail
konu="Konu"
icerik = "Metin"
resimler = ['']

gmail = "kazim.choshkun97@gmail.com"
sifre = "atakan1234"

gonder(maillerim,konu,icerik,resimler,gmail,sifre)
