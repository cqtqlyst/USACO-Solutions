'''
num,numofflowers=input().split()
num=int(num)
numofflowers=int(numofflowers)
array=[0]*num
for i in range(numofflowers):
    starti,interval=input().split()
    starti=int(starti)
    interval=int(interval)
    starti-=1
    while starti<num:
        array[starti]=1
        starti+=interval
ctr=0
for i in range(num):
    if array[i]==0:
        ctr+=1
print(ctr)

n=int(input())
array=[0]*n
array=[int(i) for i in input().split()]
i=n
while i>-1:
    if array[i]>0:
        days=array[i]
        for j in range(days-1,-1,-1):
            if array[i-1]>-1 and array[i-1]!=j:
                x=1
                break
            array[i-1]=j
            i-=1
    if array[i]==-1 or array[i]==0:
        i-=1
    if x==1:
        break
if x==1:
    print(-1)
m=0
M=0
for i in range(n):
    if array[i]==0:
        m+=1
for i in range(n):
    if array[i]==0 or array[i]==-1:
        M+=1
print(m,M)
'''
    
        