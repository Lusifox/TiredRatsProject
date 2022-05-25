f = open("z5.txt")

L = []
for line in f:
    L += map(int, line.split())

mx = -100000000
for i in L:
    if i > mx:
        mx = i
print(mx)

f.close()
