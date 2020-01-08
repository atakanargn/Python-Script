palOnceki=0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        pal=i*j
        pal=str(pal)
        palStr=str(pal[::-1])
        if(palStr==pal):
            pal=int(pal)
            if(pal>palOnceki):
                palOnceki=pal
print(palOnceki)