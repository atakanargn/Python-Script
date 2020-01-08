for a in range(3,1000,1):
    for b in range (a + 1, 999):
        cKaresi = a**2 + b**2
        c = cKaresi**0.5

        if a + b + c == 1000:
            sonuc = int(a * b * c)
            print(sonuc)
            break