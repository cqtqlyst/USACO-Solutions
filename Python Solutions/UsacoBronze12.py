'''
numofnum,numofcommands=input().split()
numofnum=int(numofnum)
numofcommands=int(numofcommands)
summy=0
array=[0]*numofnum
for i in range(numofnum):
    array[i]=int(input())
for i in range(numofcommands):
    index1,index2=input().split()
    index1=int(index1)-1
    index2=int(index2)-1
    for i in range(index1,index2+1):
        summy=summy+array[i]
    print(summy)
    summy=0
'''
array,array2=input().split()
array=list(array)
array2=list(array2)
size=len(array)
size2=len(array2)
sm=0
for i in range(size):
    array[i]=int(array[i])
for i in range(size2):
    array2[i]=int(array2[i])
for i in range(size):
    for x in range(size2):
        sm=sm+(array[i]*array2[x])
print(sm)