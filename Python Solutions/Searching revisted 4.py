'''
def bs(arr,num,find):
    mini=0
    maxi=num-1
    while mini<=maxi:
        midi=(mini+maxi)//2
        if find>array[midi]:
            mini=midi+1
        elif find<array[midi]:
            maxi=midi-1
        elif find==array[midi]:
            if midi>0 and array[midi-1]==find:
                    maxi=midi-1
            else:
                return midi
    return -1
arraysize,numofsearch=input().split()
arraysize=int(arraysize)
numofsearch=int(numofsearch)
if arraysize>0:
    array=[0]*arraysize
    array=[int(i) for i in input().split()]
    for i in range(numofsearch):
        question=int(input())
        print(bs(array,arraysize,question))
else:
    for i in range(numofsearch):
        print(-1)
'''
def bs(array,num,find):
    mini=0
    maxi=num-1
    while mini<=maxi:
        midi=(mini+maxi)//2
        if array[midi]>find:
            if midi>=1 and array[midi-1]>find:
                maxi=midi-1
            elif array[midi-1]==find:
                return midi
            else:
                return midi
        elif array[midi]<find:
            mini=midi+1
        elif array[midi]==find:
            return midi+1
    return midi+1
numofbeats,numofquestions=input().split()
numofbeats=int(numofbeats)
numofquestions=int(numofquestions)
beats=[0]*numofbeats
for i in range(numofbeats):
    beats[i]=int(input())
start=[0]*numofbeats
total=0
for i in range(numofbeats):
    start[i]=total
    total+=beats[i]
for i in range(numofquestions):
    question=int(input())
    print(bs(start,numofbeats,question))
'''
    for i in range(numofbeats):
        if question<end[i]:
            print(i+1)
            break
        if question==end[i]:
            print(i+2)

numofcows,length=input().split()
numofcows=int(numofcows)
length=int(length)
array=[0]*numofcows
for i in range(numofcows):
    array[i]=int(input())
ctr=0
array.sort()
end=numofcows-1
for start in range(numofcows):
    if array[start]+array[end]>length:
        end=end-1
    elif array[start]+array[end]<=length:
        ctr+=end-start-1
    if start==end:
        break
print(ctr)
'''