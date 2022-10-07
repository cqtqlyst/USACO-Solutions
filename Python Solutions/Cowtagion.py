def comp(c):
    return a[0]
n=int(input())
array=[0]*(n-1)
connections=[0]*n
for i in range(n):
    connections[i]=[]
for i in range(n-1):
    one,two=input().split()
    one=int(one)
    two=int(two)
    array[i]=one-1,two-1
    connections[one-1].append(two-1)
    connections[two-1].append(one-1)
check=[0]*n
check[0]=1
currentfarm=0
totaltime=0
currentlist=[]
unchecked=0
while True:
    for i in range(len(connections[currentfarm])):
        if check[connections[currentfarm][i]]==0:
            unchecked+=1
            check[connections[currentfarm][i]]=1
            currentlist.append(connections[currentfarm][i])
    sick=1
    while True:
        if sick>=unchecked+1:
            break
        else:
            sick=sick*2
            totaltime+=1
    totaltime+=unchecked
    currentfarm=currentlist[len(currentlist)-1]
    currentlist.pop()
    unchecked=0
    x=0
    for i in range(n):
        if check[i]==0:
            x=1
            break
    if x==0:
        break
print(totaltime)