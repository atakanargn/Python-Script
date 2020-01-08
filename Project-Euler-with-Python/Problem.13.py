dosya=open('Problem.13.sayi.txt','r')
say=dosya.read()

for i in range(0,101,1):
    sayi=say.split('\n')

toplam=0

for i in range(0,100,1):
    sayim=sayi[i][0:12]
    sayim=int(sayim)
    toplam+=sayim

toplam=str(toplam)
print(toplam[:10])