n,k=input().split()
n=int(n)
k=int(k)
swap=[0]*k
for i in range(k):
    a,b=input().split()
    a=int(a)
    b=int(b)
    swap[i]=a,b
array=[0]*(n+1)
matrix=[0]*(n+1)
for i in range(1,n+1):
    matrix[i]=set()
for i in range(1,n+1):
    array[i]=i
x=0
while True:
    for i in range(k):
        swapper=array[swap[i][0]]
        array[swap[i][0]]=array[swap[i][1]]
        array[swap[i][1]]=swapper
        matrix[array[swap[i][0]]].add(i)
        matrix[array[swap[i][1]]].add(i)
    for i in range(1,n+1):
        if array[i]!=i:
            x=1
    if x==0:
        break
    x=0
for i in range(1,n+1):
    sume=len(matrix[i])
    if sume>0:
        print(sume)
    else:
        print(1)