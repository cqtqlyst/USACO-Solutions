'''
def dist(x1,y1,x2,y2):
    return abs(x2-x1) + abs(y2-y1)
n=int(input())
arr=[0]*(n+1)
for i in range(1,n+1):
    x,y=input().split()
    x=int(x)
    y=int(y)
    arr[i]=x,y
sumer=0
for i in range(1,n):
    sumer+=dist(arr[i][0],arr[i][1],arr[i+1][0],arr[i+1][1])
ans=sumer
for i in range(2,n):
    curval=sumer-dist(arr[i][0],arr[i][1],arr[i-1][0],arr[i-1][1])-dist(arr[i][0],arr[i][1],arr[i+1][0],arr[i+1][1])+dist(arr[i-1][0],arr[i-1][1],arr[i+1][0],arr[i+1][1])
    ans=min(ans,curval)
print(ans)

n=int(input())
freq=[0]*676
for i in range(676):
    freq[i]=[0]*676
for i in range(n):
    city,state=input().split()
    newcity=city[:2]
    city=newcity
    citynum=(ord(city[0])-ord('A'))*26+(ord(city[1])-ord('A'))
    statenum=(ord(state[0])-ord('A'))*26+(ord(state[1])-ord('A'))
    freq[citynum][statenum]+=1
sumi=0
for i in range(676):
    for j in range(676):
        if i<j:
            sumi+=freq[i][j]*freq[j][i]
print(sumi)

n=int(input())
array=[0]*n
for i in range(n):
    array[i]=int(input())
index=0
owed=0
currentbal=0
leftmostowed=n
dist=0
while True:
    if array[index]>0:
        currentbal+=array[index]
        index+=1
        dist+=1
    elif array[index]<0:
        if index<leftmostowed:
            leftmostowed=index
        owed+=array[index]
        index+=1
        dist+=1
    if currentbal-owed>=0 and leftmostowed!=n:
        for i in range(index,leftmostowed,-1):
            dist+=1
    if index==n-1:
        break
print(dist)
'''
n=int(input())
height=[0]*(n+1)
for i in range(1,n+1):
    height[i]=int(input())
left=[0]*(n+1)
right=[0]*(n+1)
curleft=1
for i in range(1,n+1):
    if height[i]<height[i+1]:
        curleft=i
    left[i]=curleft
curright=n
for i in range(n,0,-1):
    if height[i]<height[i-1]:
        curright=i
    right[i]=curright
ans=0
for i in range(1,n+1):
    ans=max(ans,right[i]-left[i]+1)