#CEVAP 9 BASAMAKLI, O YÜZDEN 100000000DEN BAŞLATTIM
sayi=100000000
kapat=False

while True:
    sayi+=1
    for i in range(1,21,1):
        if(sayi%i==0):
            kapat=True
            continue
        else:
            kapat=False
            break
    
    if(kapat==True):
        break
print(sayi)