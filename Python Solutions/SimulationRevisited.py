'''
n=int(input())
ctrarr=[0]*7
dow=1
for i in range(1900,1900+n):
    for j in range(1,13):
        if j==4 or j==6 or j==9 or j==11:
            numofdays=30
        elif j==2:
            if i%400==0 or (i%4==0 and i%100!=0):
                numofdays=29
            else:
                numofdays=28
        else:
            numofdays=31
        for d in range(1,numofdays+1):
            dow=(dow+1)%7
            if d==13:
                ctrarr[dow]+=1
for i in range(7):
    print(ctrarr[i] ,end=" ")

numofl,numofb=input().split()
numofl=int(numofl)
numofb=int(numofb)
l=[0]*100
b=[0]*100
currentindex=0
for i in range(numofl):
    time,speed=input().split()
    time=int(time)
    speed=int(speed)
    for j in range(currentindex,currentindex+time):
        l[j]=speed
    currentindex+=time
currentindex=0
for i in range(numofb):
    time,speed=input().split()
    time=int(time)
    speed=int(speed)
    for j in range(currentindex,currentindex+time):
        b[j]=speed
    currentindex+=time
maxi=0
for i in range(100):
    if b[i]-l[i]>maxi:
        maxi=b[i]-l[i]
print(maxi)
'''
num=int(input())
array=[0]*num
for i in range(num):
    array[i]=int(input())
array.sort()
maxi=0
ctr=0
for i in range(num):
    r=1
    posl=i
    posr=i
    indexr=i+1
    indexl=i-1
    while True:
        origl=indexl
        origr=indexr
        if posr<num-1:
            while indexr<num and array[posr]+r>=array[indexr]:
                indexr+=1
                ctr+=1
            posr=indexr-1
        if posl>0:
            while indexl>-1 and array[posl]-r<=array[indexl]:
                indexl-=1
                ctr+=1
            posl=indexl+1
        r+=1
        if indexr==origr and indexl==origl:
            break
    if ctr>maxi:
        maxi=ctr
    print(ctr)
    ctr=0
print(maxi+1)
'''
num=int(input())
array=[0]*num
for i in range(num):
    array[i]=int(input())
array.sort()
ctr=0
maxi=0
for i in range(num):
    posr=i
    while True:
        add=1
        while True:
            if posr+add<num and arr[posr]+r>=array[posr+add]:
                ctr+=1
                add+=1
            else:
                break
        if add!=1:
            posr=posr+add-1
            r+=1
        else:
            break
    posl=i
    while True:
        add=1
        while True:
            if posr-add>0 and arr[posl]-r<=array[posl-add]:
                ctr+=1
                add+=1
            else:
                break
        if add!=1:
            posl=posl-add+1
            r+=1
        else:
            break
    if ctr>maxi:
        maxi=ctr
print(maxi)

num=int(input())
array=[0]*num
for i in range(num):
    array[i]=int(input())
array.sort()
maxi=0
ctr=0
for i in range(num):
    r=1
    posl=i
    posr=i
    index=i+1
    if i<num-1:
        while True:
            orig=index
            while index<num and array[posr]+r>=array[index]:
                index+=1
                ctr+=1
            if index==orig or index==num:
                break
            posr=index-1
            r+=1
    index=i-1
    r=1
    if i>0:
        while True:
            orig=index
            while index>-1 and array[posl]-r<=array[index]:
                index-=1
                ctr+=1
            if index==orig or index==0:
                break
            posl=index+1
            r+=1
    if ctr>maxi:
        maxi=ctr
    ctr=0
print(maxi+1)
'''