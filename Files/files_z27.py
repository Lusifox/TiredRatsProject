from random import *
seed()
n=randint(3,7)


f=open("file.txt","w")
for i in range(n):
    x=randint(-10,10)
    x=str(x)+" "
    f.write(x)

f.close()

f=open("file.txt","r")
t=f.read()
k=t.split()
f.close()

g=open("file_obrat.txt","w")

for i in range(n-1,-1,-1):
    x=k[i]
    x=x+" "
    g.write(x)

g.close()
