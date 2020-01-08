a,b=1,1
toplam=0
while(b<=4000000):
    a,b=b,a+b
    if(b%2==0):
        toplam+=b
print(toplam)