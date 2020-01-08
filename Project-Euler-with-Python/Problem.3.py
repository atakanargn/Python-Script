sayi=600851475143
for i in range(2,sayi,1):
    if(sayi%i==0):
        bolundu = False
        for j in range(2,i):
            if i % j == 0:
                bolundu=True
                
        if bolundu == False:
            print("ASAL : "+str(i))
