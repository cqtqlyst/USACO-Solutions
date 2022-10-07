'''
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s1=input()
s2=input()
result1=1
result2=1
num=0
for i in range(len(s1)):
    num=alph.find(s1[i])
    result1=result1*(num+1)
for i in range(len(s2)):
    num=alph.find(s2[i])
    result2=result2*(num+1)
if result1%47==result2%47:
    print("GO")
else:
    print("STAY")

alph="abcdefghijklmnopqrstuvwxyz"
num=int(input())
side1arr=[0]*26
side2arr=[0]*26
array=[0]*26
for i in range(num):
    side1,side2=input().split()
    side1arr=[0]*26
    side2arr=[0]*26
    for x in range(len(side1)):
        index=alph.find(side1[x])
        side1arr[index]+=1
    for y in range(len(side2)):
        index=alph.find(side2[y])
        side2arr[index]+=1
    for b in range(26):
        array[b]+=max(side1arr[b],side2arr[b])
for i in range(26):
    print(array[i])
'''
num,numofcol=input().split()
num=int(num)
numofcol=int(numofcol)
spottyarr=[0]*num
nonarr=[0]*num
boolarr=[0]*num
counter=0
flag=0
for i in range(num):
    spottyarr[i]=input()
for i in range(num):
    nonarr[i]=input()
for i in range(numofcol):
    boolarr=[0]*num
    flag=0
    for j in range(num):    
        c=spottyarr[j][i]
        for x in range(num):
            c2=nonarr[x][i]
            if c==c2:
                flag=1
            else:
                
















