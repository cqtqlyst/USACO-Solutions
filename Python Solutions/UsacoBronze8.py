'''
x,y=input().split()
x=int(x)
y=int(y)
for i in range(1,x+1):
    if x%i==0:
        for a in range(1,y+1):
            if y%a==0:
                print(i,end=" ")
                print(a)
'''
numofnum=int(input())
arrayx=[0]*2001
arrayy=[0]*2001
minimum=1000000000000000000000000000000
cowid=""
for i in range(1,numofnum+1):
    x,y=input().split()
    x=int(x)
    y=int(y)
    arrayx[i]=x
    arrayy[i]=y
for i in range(1,numofnum):
    for e in range(i,numofnum+1):
        currentx=abs(arrayx[i]-arrayx[e])
        currenty=abs(arrayy[i]-arrayy[e])
        actual=currentx**2+currenty**2
        if actual!=0:
            if actual<minimum:
                minimum=actual
                cowid=""
                cowid=str(i)+" "+str(e)
print(cowid)
        