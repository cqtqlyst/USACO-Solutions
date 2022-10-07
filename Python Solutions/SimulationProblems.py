'''
goal,numofcows=input().split()
goal=int(goal)
numofcows=int(numofcows)
crt=0
totaltime=0
readpages=0
for i in range(numofcows):
    readingspeed,timebfrest,resttime=input().split()
    readingspeed=int(readingspeed)
    timebfrest=int(timebfrest)
    resttime=int(resttime)
    while readpages<goal:
        readpages=readpages+readingspeed
        totaltime=totaltime+1
        crt=crt+1
        if readpages>=goal:
            print(totaltime)
            break
        elif crt==timebfrest:
            crt=0
            totaltime=totaltime+resttime
    crt=0
    resttime=0
    readpages=0
    totaltime=0

numofnum,numoftimes=input().split()
numofnum=int(numofnum)
numoftimes=int(numoftimes)
array=[0]*numofnum
for i in range(numofnum):
    array[i]=int(input())
maxi=0
indvalue=0
remaining=0
count=0
for i in range(numoftimes):
    for j in range(numofnum):
        if array[j]>maxi:
            maxi=array[j]
            indvalue=j
    print(indvalue+1)
    array[indvalue]=0
    remaining=maxi%(numofnum-1)
    distr=maxi//(numofnum-1)
    for j in range(numofnum):
        if j!=indvalue:
            array[j]=array[j]+distr
    for j in range(numofnum):
        if remaining==0:
            break
        if j!=indvalue:
            array[j]=array[j]+1
            remaining=remaining-1
'''    
numsize,arrsize=input().split()
numsize=int(numsize)
arrsize=int(arrsize)
elimarr=[0]*arrsize
elimarr=[int(i) for i in input().split()]
arr=[0]*numsize
for i in range(numsize):
    arr[i]=i+1
n=1
count=0
i=0
j=0
while n==1:
    i=(i+1)%numsize
    j=(j+1)%arrsize
    for a in range(numsize):   
        if arr[a]!=0:
            count+=1
    if count==elimarr[j]:
        arr[i]=0
    if count==1:
        for a in range(numsize):
            if arr[a]>0:
                print(arr[a])
    