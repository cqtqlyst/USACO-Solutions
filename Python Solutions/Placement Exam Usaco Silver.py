'''
c,b=input().split()
c=int(c)
b=int(b)
array=[0]*b
array=[int(i) for i in input().split()]
newarray=[0]*(b+1)
for i in range(b):
    newarray[i]=array[i]
newarray[b]=0
allsums=[0]*(b**2)
a=0
maxe=0
for i in range(b):
    for j in range(i,b+1):
        allsums[a]=newarray[i]+newarray[j]
        a+=1
for i in range(b**2):
    for j in range(i,b**2):
        current=allsums[i]+allsums[j]
        if current<c and current>maxe:
            maxe=current
print(maxe)

import math
def prime(n):
    arr=[0]*int(math.sqrt(n))
    j=0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            arr[j]=i
            j+=1
    return arr
s=int(input())
while True:
    total=0
    root=int(math.sqrt(s))
    array=prime(s)
    for i in range(root):
        if array[i]!=0:
            total+=array[i]+(s//array[i])
    total-=s
    total2=0
    root2=int(math.sqrt(total))
    array2=prime(total)
    for i in range(root2):
        if array2[i]!=0:
            total2+=array2[i]+(total//array2[i])
    total2-=total
    if total2==s:
        break
    s+=1
print(total2,total)
'''
rows,cols,squares=input().split()
rows=int(rows)
cols=int(cols)
squares=int(squares)
matrix=[0]*rows
for i in range(rows):
    matrix[i]=[0]*cols
array=[0]*100000
a=0
for i in range(rows):
    matrix[i]=[j for j in input().split()]
if squares<(rows+cols-1):
    print(0)
else:
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]=="T":
                row=rows-i-1
                col=j+1
                array[a]=(math.factorial(row+col)//(math.factorial(col)*math.factorial(row)))*(math.factorial(rows-row-1+cols-col-1)//(math.factorial(rows-row-1)*math.factorial(cols-col-1)))
                a+=1
total=0
for i in range(100000):
    total+=array[i]
