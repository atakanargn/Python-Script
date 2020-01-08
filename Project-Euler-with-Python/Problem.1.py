toplam=0
for i in range(0,1000,1):
    if(i%3==0 or i%5==0):
        toplam+=i
print(toplam)