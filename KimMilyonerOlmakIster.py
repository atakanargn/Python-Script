# Yazar : Atakan Argın
# Github : atakanargn
# Çalıştırmadan önce boş bir sorular.txt oluşturulmalı!

# *** Joker hakları gelecek...


# time kütüphanesi içinden
# sadece sleep() fonksiyonunu çektik
from time import sleep

# rastgele sayı üretmek için gereken random kütüphanesinden
# sadece randint() fonksiyonunu çektik
from random import randint

# Işletim sistemi ile ilgili işlem
# yapmaya yarayan os kütüphanesinden
# sadece system() fonksiyonunu çektik
from os import system

# Şifre girerken karakterlerin gözükmemesini
# sağlayan getpass kütüphanesi
from getpass import getpass

while True:
	#Giriş menüsü
	print("### Kim Milyoner Olmak Ister !? ###\n"+
		  "# Hoşgeldin, Bitcoin Milyoneri\n"+
		  "# olmak ister misin ?\n"+
		  "# Seç ve başla!\n"+
		  "# 1) Evet, başlayalım!\n"+
		  "# 2) Soru eklemeye geldim!!!\n"+
		  "# 3) ÇIKIŞ !")
	menuSec1 = int(input(">>> "))

	# Ekranı temizlemek için kullanılan fonksiyon;
	# Hem windowsta hem de Linuxta çalışıyor
	system("cls,clear;clear")
	

	if(menuSec1 == 1):
		isim = input("  Adınızı ve soyadınızı girin (Örn: Atakan Argın)\n>> ")
		# Ekranı temizle
		system("cls,clear;clear")

		# Sorular dosyasını okuma kipinde aç
		dosya = open("sorular.txt","r")
		# Dosya içindeki tüm satırları
		# "sorular" dizisine at
		sorular = dosya.readlines()
		# Dosyayı kapat
		dosya.close()

		# Sorular dizisini saydırıyoruz
		say = 0
		for soru in sorular:
			say += 1
		
		i = 0
		# Verilecek Bitcoinler
		vPuanlar = [0.0025, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 0.75, 1]

		puan=0
		hata = ""
		#10 soru olmasını istedik
		while(i <= 10):
			i+=1
			# Sorular dosyasında;
			# 1. Satır = Sorunun içeriği
			# 2. Satır = A şıkkı
			# 3. Satır = B şıkkı
			# 4. Satır = C şıkkı
			# 5. Satır = D şıkkı
			# 6. Satır = Sorunun cevabı
			
			# Bu yüzden soru seçmek için;
			# saydırdığımız değişkeni 6'ya böldük
			# 0'dan çıkan değere kadar rastgele 1 sayı seçtik
			sorusayi = (randint(0,(int(say/6)-1))*6)

			system("cls,clear;clear")
			# Hata varsa yazdır
			print(hata)
			# 30 tane "#" yazdırdı
			print(30*"#"+"\n")
			# Kaçıncı soru olduğunu yazdırdık
			print("  Soru "+str(i)+"\n    "+str(sorular[sorusayi]))
			# 30 tane "#" yazdırdı
			print(30*"#"+"\n")
			aSikki = sorular[sorusayi+1]
			print("  A) "+aSikki)
			bSikki = sorular[sorusayi+2]
			print("  B) "+bSikki)
			cSikki = sorular[sorusayi+3]
			print("  C) "+cSikki)
			dSikki = sorular[sorusayi+4]
			print("  D) "+dSikki)
			cevap = sorular[sorusayi+5]
			print(cevap)

			while True:
				kCevap = input("  Cevabınız nedir ? [A, B, C, D]\n  >> ")
				# kCevap büyük harf girildiyse küçültür
				kCevap = kCevap.lower()
				sonKarar = input("  SON KARARIN MI ? ( [E] / H )\n  >> ")
				# sonKarar büyük harf girildiyse küçültür
				sonKarar = sonKarar.lower()
				if(sonKarar == 'e'):
					break
				elif(sonKarar == 'h'):
					continue
				else:
					print("  HATALI GİRİŞ!")

			if(kCevap == cevap[:1]):
				puan+=float(vPuanlar[i-1])
				print(30*"#"+"\n")
				print("  Doğru bildiniz! "+str(vPuanlar[i-1])+" BTC kazandınız,\n  Bununla beraber bakiyeniz "+str(puan))
				print(30*"#"+"\n\n")
				print("  DEVAM ETMEK ISTER MISIN ?\n")
				print("  1 -> Evet, daha fazla BTC !!")
				print("  2 -> Hayır, bu kadar BTC yeterli...")
				menum = int(input(">>> "))
				print(30*"#"+"\n")
				if(menum == 2):
					print(30*"#"+"\n")
					print("  YARIŞMADAN %0.4f BTC KAZANDIN, TEBRİKLER %s !"%(puan,isim.upper()))
					print(30*"#"+"\n")
					break
			else:
				i=10
				print(30*"#"+"\n")
				print("  Cevabın yanlış !!!\n  OYUN BİTTİ!")
				print("  YARIŞMADAN %0.4f BTC KAZANDIN, TEBRİKLER %s !"%(puan/2,isim.upper()))
				print(30*"#"+"\n")
				break
				



	elif(menuSec1==2):
		sifre=getpass("O zaman şifre : ")
		if(sifre=="sifre"):
			dosya=open("sorular.txt","r")
			sorular=dosya.readlines()
			dosya.close()
			say=0
			for soru in sorular:
				say+=1
			print("Oyunda kayıtlı *"+str(int(say/6))+"* adet soru var!\n")
			while True:
				dosya=open("sorular.txt","r+")	
				for soru in sorular:
					dosya.write(soru)
				soruIcerik=input("Soruyu girin\n>> ")
				dosya.write(soruIcerik+"\n")
				soruA=input("A şıkkını girin\n>> ")
				dosya.write(soruA+"\n")
				soruB=input("B şıkkını girin\n>> ")
				dosya.write(soruB+"\n")
				soruC=input("C şıkkını girin\n>> ")
				dosya.write(soruC+"\n")
				soruD=input("D şıkkını girin\n>> ")
				dosya.write(soruD+"\n")
				cevap=input("Cevabı girin\n>> ")
				dosya.write(cevap+"\n")
				dosya.close()

				devamMi=input("Devam mı ? ( E / [H] )\n>> ")
				if(devamMi=='E' or devamMi=='e'):
					continue
				else:
					break
	elif(menuSec1==3):
		print("BİTTİ!!")
		break
	else:
		print("Böyle bir seçenek yok!\nTekrar seçim yap!\n\n")