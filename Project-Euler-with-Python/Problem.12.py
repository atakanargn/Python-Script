def tamBolenSayi(n):
    if(n % 2 == 0):
        n = n/2
    bolen = 1
    sayac = 0
    while(n % 2 == 0):
        sayac += 1
        n = n/2
    bolen = bolen * (sayac + 1)
    p = 3
    while(n != 1):
        sayac = 0
        while(n % p == 0):
            sayac += 1
            n = n/p
        bolen = bolen * (sayac + 1)
        p += 2
    return bolen
 
def bul(limit):
    n = 1
    lnum, rnum = tamBolenSayi(n), tamBolenSayi(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, tamBolenSayi(n+1)
    return n

cevap1 = bul(500)
sonuc = int((cevap1 * (cevap1 + 1)) / 2)

print(sonuc)