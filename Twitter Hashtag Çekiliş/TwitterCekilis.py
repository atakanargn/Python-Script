#Twitter Lottery Script
#Author : Atakan Argın
#Github : argin-atakan
from twython import Twython
from time import sleep
from re import split
from os import path
from random import randint

"""
1) twitterda uygulama oluştur
2) tokenleri ve secret keyleri yaz
"""

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_SECRET'

#Twitter'a bağlantı
twitter = Twython(app_key=consumer_key,
		  app_secret=consumer_secret,
		  oauth_token=access_token,
		  oauth_token_secret=access_token_secret)

print(10*"#"+"Twitter Çekiliş"+10*"#"+"\n\tYazar : Atakan Argın\n")
while True:
	islem=int(input("\t1) Katılımcı ekle\n\t2) Çekilişi yap\n seçimini yap >> "))
	
	#Katılımcı ekle
	if(islem==1):
		listedeMi=False
		hashtag=input("\n HASHTAG >> ")

		cnt=int(input(" Dakikada kaç tweet aramak istersin ?\n>> "))
		print("\n")
		#Dosya varlığı kontrolü
		if(path.isfile("cekilis.txt")==False):
			dosya=open("cekilis.txt","w")
			dosya.write("\n")
			dosya.close()
		
		i=0
		while 1:
			i+=1

			#Tweetleri çek
			ara = twitter.search(q='#'+str(hashtag), count=cnt)
			tweetler = ara['statuses']
			
			for tweet in tweetler:
				dosya=open("cekilis.txt","r+")
				eski=dosya.readlines()

				for katilimci in eski:

					#Katılımcı listede mi ?
					if(katilimci[:-1]==tweet['user']['screen_name']):
						listedeMi=True

				#Katılımcı listede yoksa
				if(listedeMi!=True):
					#Listeye ekle
					dosya.write(str(tweet['user']['screen_name'])+"\n")
					print(str(tweet['user']['screen_name'])+" adlı kullanıcı listeye eklendi...")
					dosya.close()
				else:
					# listedeyse bişey yapma.
					# ya da print("Katılımcı listede!")
					listedeMi=False
			print(15*"#"+str(i)+"#"*15)

			#1 dakika bekle
			sleep(60)

	#Çekilişi yap
	elif(islem==2):
		dosya=open("cekilis.txt","r") #Katılımcı listesini oku
		isimler=dosya.readlines()
		say=-1
		for isim in isimler: #Katılımcıları say
			say+=1
		print("Katılımcı sayısı : "+str(say))
		sansliKatilimci = randint(1,say) #Choose lucky competitor
		print("Şanslı kullanıcı : "+str(isimler[sansliKatilimci]))
		dosya.close()
		break
	else:
		print("Yanlış seçim!\nTekrar dene!!\n\n")
