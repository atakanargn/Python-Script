def collatz(n):
    count=1
    while(n>1):
        count+=1
        if(n%2==0):
            n=n/2
        else:
            n=3*n+1
    return count

sayi = [0,0]

for i in range(1000000):
    c=collatz(i)
    if(c>sayi[0]):
        sayi[0]=c
        sayi[1]=i

print(sayi[1])