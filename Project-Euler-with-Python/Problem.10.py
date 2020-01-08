toplam=0
for i in range(1,2000001,1):
    print(i)
    bolundu=False
    for j in range(2,i,1):
        if(i%j==0):
            bolundu=True
    if(bolundu==False):
        toplam+=i
print(toplam)