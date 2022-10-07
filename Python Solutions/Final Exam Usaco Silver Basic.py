'''
def funct(loc,inc):
    global maxi
    if inc==0:
        return
    if loc+inc>maxit or loc-inc<0:
        return
    sume=0
    for i in range(n):
        if ranges[i][0]<=loc and loc<=ranges[i][1]:
            sume+=y
        if loc<ranges[i][0]:
            sume+=x
        if loc>ranges[i][1]:
            sume+=z
    maxi=max(sume,maxi)
    funct(loc+inc,inc//2)
    funct(loc-inc,inc//2)

n,x,y,z=input().split()
n=int(n)
x=int(x)
y=int(y)
z=int(z)
ranges=[0]*n
maxit=0
maxi=0
for i in range(n):
    start,end=input().split()
    start=int(start)
    end=int(end)
    ranges[i]=start,end
    maxit=max(maxit,end)
for loc in range(maxit):
    sume=0
    for j in range(n):
        if ranges[j][0]<=loc and loc<=ranges[j][1]:
            sume+=y
        if loc<ranges[j][0]:
            sume+=x
        if loc>ranges[j][1]:
            sume+=z
    maxi=max(maxi,sume)
print(maxi)

def combogen(e,cnt):
    global elements
    global number
    global m
    global n
    global array
    if e==m and cnt==n:
        process()
        return
    elif e==m and cnt!=n:
        return
    else:
        elements[e]=1
        combogen(e+1,cnt+1)
        elements[e]=0
        combogen(e+1,cnt)
def process():
    sume=0
    strsum=str(sume)
    for i in range(m):
        if elements[i]==1:
            strarr=str(array[i])
            for j in range(1,min(len(strarr),len(strsum))+1)
                indexi=len(strarr))-j
                indexs=len(strsum)-j
                inti=int(strarr[indexi])
                ints=int(strsum[indexs])
                if inti+ints>=10:
                    return
    maxi=max(n,maxi)
m=int(input())
array=[0]*m
for i in range(m):
    array[i]=int(input())
elements=[0]*m
maxi=0
for n in range(1,m+1):
    combogen(0,0)
print(maxi)

def rec(currentcow):
    global total
    global used
    total+=array[currentcow][0]
    used[currentcow]=1
    for i in range(array[currentcow][1]):
        if used[m[currentcow][i]]==0:
            rec(m[currentcow][i])
line = input().split()
pos = 0
def readInt():
    global pos, line
    if pos >= len(line):
        line = input().split()
        pos = 0
    pos += 1
    return int(line[pos - 1])
n=readInt()
array=[0]*(n+1)
m=[]*(n+1)
for i in range(1,n+1):
    l=readInt()
    mi=readInt()
    array[i]=l,mi
    for j in range(mi):
        hi=readInt()
        m[i].append(hi)
total=0
used=[0]*n
currentcow=1
rec(1)
'''