'''
n=int(input())
string=input()
prefixsum=[0]*n
for i in range(n):
    prefixsum[i]=[0]*3
numo=0
numw=0
for i in range(n-1,-1,-1):
    if string[i]=="W":
        numw+=1
    if string[i]=="O":
        numo+=1
    prefixsum[i][0]=numw
    prefixsum[i][1]=numo
total=0
for i in range(n):
    if string[i]=="C":
        for j in range(i,n):
            if string[j]=="O":
                total+=prefixsum[j][0]
print(total)
'''
def comp(c):
    return c[0]
n=int(input())
array=[0]*n
array2=[0]*n
for i in range(n):
    array[i]=[0]*4
    array2[i]=[0]*4
for i in range(n):
    print(i)
    arrival,timespent=input().split()
    arrival=int(arrival)
    timespent=int(timespent)
    timewaited=0
    array[i][0]=arrival
    array[i][1]=timespent
    array[i][2]=i
    array[i][3]=timewaited
    array2[i][0]=arrival
    array2[i][1]=timespent
    array2[i][2]=i
    array2[i][3]=timewaited
array.sort(key=comp)
currentcowend=array[0][0]+array[0][1]
waitinglist=[]
for i in range(n):
    print(array[i][2])
i=1
while True:
    if array[i][0]<=currentcowend:
        waitinglist.append(array[i][2])
        waitinglist.sort()
    elif array[i][0]>currentcowend:
        index=0
        while True:
            array2[waitinglist[index]][3]=currentcowend-array2[waitinglist[index]][0]
            currentcowend=currentcowend+array2[waitinglist[index]][1]
            waitinglist.reverse()
            waitinglist.pop()
            waitinglist.reverse()
            if len(waitinglist)==0:
                break
        currentcowend=array[i][0]+array[i][1]
    i+=1
    if i==n:
        break
maxi=0
for j in range(n):
    if array2[j][3]>maxi:
        maxi=array2[j][3]
print(maxi)
        