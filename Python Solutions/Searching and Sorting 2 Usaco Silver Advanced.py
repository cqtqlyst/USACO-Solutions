n,k=input().split()
n=int(n)
k=int(k)
array=[0]*n
for i in range(n):
    array[i]=int(input())
array.sort()
small=[0]*n
left=0
right=0
bestscore=0
index=0
while True:
    if array[right]-array[left]<=k:
        right+=1
    elif array[right]-array[left]>k:
        while True:
            left+=1
            if array[right]-array[left]<=k:
                break
    bestscore=max(bestscore,left-right)
    small[index]=bestscore
    index+=1
    if index>n-1:
        break
    if right==n-1:
        break
big=[0]*n
right=n-1
left=n-1
bestscore=0
index=n-1
while True:
    if array[right]-array[left]<=k:
        left-=1
    elif array[right]-array[left]>k:
        while True:
            right-=1
            if array[right]-array[left]<=k:
                break
    bestscore=max(bestscore,right-left)
    big[index]=bestscore
    index-=1
    if index<0:
        break
    if left==0:
        break
maxi=0
for i in range(n-1):
    if small[i]+big[i+1]>maxi:
        maxi=small[i]+big[i+1]
print(maxi)