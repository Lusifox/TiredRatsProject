from random import *
seed()
n=randint(3,7)



f=open("int.txt", "wb")
for i in range(n):
    x=randint(-10,10)

    bx=x.to_bytes(2,byteorder="little",signed=True)
    f.write(bx)

f.close()



f=open("int.txt", "rb")

bx=f.read(2)
k=[]

while bx!=b'':
    x=int.from_bytes(bx, byteorder="little",signed=True)
    print(x)
    k.append(x)
    bx=f.read(2)
f.close()

a=[]
s=0
j=0
i=0
g=0
while(i<len(k)):

    j=i
    while(j<len(k) and k[j]>0):
        s=s+k[j]
        j=j+1
        g=g+1

    j=i
    while(j<len(k) and k[j]<0):
        s=s+k[j]
        j=j+1
        g=g+1
    j=i
    while(j<len(k) and k[j]==0):
        s=s+k[j]
        j=j+1
        g=g+1
        
    a.append(s)
    s=0
    
    i=i+g
    g=0

print(a)

t=open("res.txt", "wb")
for i in range(0,len(a)):
    x=a[i]
    print(x)
    tx=x.to_bytes(2,byteorder="little",signed=True)
    t.write(tx)

t.close()


























