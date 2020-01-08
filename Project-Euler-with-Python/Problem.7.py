sayi=1
sayac=1   

while(sayac<=10001):
    sayi+=1

    bolundu = False
    for j in range(2,sayi,1):
        if(sayi % j == 0):
            bolundu=True

    if(bolundu == False):
        print(sayi)
        sayac+=1