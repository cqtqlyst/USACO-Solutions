n=int(input())
m=[0]*n
for i in range(n):
    m[i]=[0]*n
for i in range(n):
    for j in range(n):
        m[i][j]=[]
x=[]
y=[]
for i in range(n):
    xarr,yarr=input().split()
    xarr=int(xarr)
    yarr=int(yarr)
    x.append(xarr)
    y.append(yarr)

    
