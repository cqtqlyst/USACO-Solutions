'''
n=int(input())
m=[0]*n
maxi=-1000000000000000000
for i in range(n):
    m[i]=[0]*n
for i in range(n):
    m[i]=[int(j) for j in input().split()]
for i in range(n):
    for j in range(n):
        currenttotal=0
        row=i
        col=j
        for g in range(n):
            currenttotal+=m[row][col]
            if currenttotal>maxi:
                maxi=currenttotal
            row-=1
            col+=1
            if row==-1:
                row=n-1
            if col==n:
                col=0
        currenttotal=0
        row=i
        col=j
        for g in range(n):
            currenttotal+=m[row][col]
            if currenttotal>maxi:
                maxi=currenttotal
            row-=1
            col-=1
            if row==-1:
                row=n-1
            if col==-1:
                col=n-1
        currenttotal=0
        row=i
        col=j
        for g in range(n):
            currenttotal+=m[row][col]
            if currenttotal>maxi:
                maxi=currenttotal
            row+=1
            if row==n:
                row=0
        currenttotal=0
        row=i
        col=j
        for g in range(n):
            currenttotal+=m[row][col]
            if currenttotal>maxi:
                maxi=currenttotal
            col+=1
            if col==n:
                col=0
print(maxi)

def check(r):
    global n
    global k
    global array
    currentpos=0
    x=0
    ctr=0
    while True:
        x=0
        length=array[currentpos]+1+(2*r)
        for i in range(currentpos,n):
            if array[i]>length:
                currentpos=i
                x=1
        ctr+=1
        if x==0:
            break
    if ctr<=k:
        return True
    return False
def bs():
    global n
    global k
    global array
    maxi=array[n-1]
    mini=0
    while mini<maxi:
        midi=(maxi+mini)//2
        if check(midi)==True:
            maxi=midi
        elif check(midi)==False:
            mini=midi+1
    return maxi
n,k=input().split()
n=int(n)
k=int(k)
array=[0]*n
for i in range(n):
    array[i]=int(input())
array.sort()
print(bs())
'''
n,a,b,c,d,e,f,g,h,m=input().split()
n=int(n)
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
g=int(g)
h=int(h)
m=int(m)
array=[0]*n
for i in range(n*3):
    current=