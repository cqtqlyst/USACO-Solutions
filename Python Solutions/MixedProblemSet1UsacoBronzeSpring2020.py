
n=int(input())
m=[0]*n
maxbeauty=-50000000000000000000
for i in range(n):
    m[i]=[0]*n
for i in range(n):
    m[i]=[int(j) for j in input().split()]
for r in range(n):
    for c in range(n):
        diag1=m[r][c]
        diag2=m[r][c]
        exp=1
        while r-exp>=0 and r+exp<=n-1 and c-exp>=0 and c+exp<=n-1:
            diag1+=m[r+exp][c+exp]+m[r-exp][c-exp]
            diag2+=m[r+exp][c-exp]+m[r-exp][c+exp]
            beauty=diag1-diag2
            if beauty>maxbeauty:
                maxbeauty=beauty
            exp+=1
            
for r in range(n):
    for c in range(n):
        diag1=0
        diag2=0
        exp=0
        while r+exp+1<=n-1 and r-exp>=0 and c+exp+1<=n-1 and c-exp>=0:
            diag1+=m[r+exp+1][c+exp+1]+m[r-exp][c-exp]
            diag2+=m[r+exp+1][c-exp]+m[r-exp][c+exp+1]
            beauty=diag1-diag2
            if beauty>maxbeauty:
                maxbeauty=beauty
            exp+=1
print(maxbeauty)
'''
num=int(input())
counters=[0]*num
x=[0]*num
y=[0]*num
r=[0]*num
for i in range(num):
    xi,yi,ri=input().split()
    xi=int(xi)
    yi=int(yi)
    ri=int(ri)
    x[i]=xi
    y[i]=yi
    r[i]=ri
for i in range(num):
    for j in range(i+1,num):
        d=(abs(x[j]-x[i])**2)+(abs(y[j]-y[i])**2)
        if d==((r[i]+r[j])**2):
            counters[i]+=1
            counters[j]+=1
for i in range(num):
    if counters[i]==1:
        if x[i]!=0 or y!=0:
            print(x[i], y[i])
            break

def comp(c):
    return c[1]
num=int(input())
array=[0]*num
for i in range(num):
    array[i]=[0]*3
for i in range(num):
    size,pos=input().split()
    size=int(size)
    pos=int(pos)
    a=0
    array[i][0]=size
    array[i][1]=pos
    array[i][2]=a
array.sort(key=comp)
for sp in range(num):
    indexl=sp
    indexr=sp+1
    while True:
        if indexl<0:
            break
        if indexr==num:
            break
        d=(array[indexr][1])-(array[indexl][1])
        if d<=array[indexr][0] and d<=array[indexl][0]:
            for j in range(indexl,indexr):
                array[j][2]=1
            break
        if d>array[indexr][0]:
            indexr+=1
        if d>array[indexl][0]:
            indexl-=1
total=0
for i in range(num):
    if array[i][2]==1:
        total+=abs(array[i][1]-array[i+1][1])
print(total)
'''