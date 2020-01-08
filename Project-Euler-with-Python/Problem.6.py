t1=0;t2=0
for i in range(1,101,1):
    print(i)
    t1+=i*i

for i in range(1,101,1):
    print(i)
    t2+=i

print((t2*t2)-t1)