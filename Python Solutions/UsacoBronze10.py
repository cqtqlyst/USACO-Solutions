'''
def finder(number,finding):
    found=str(number).find(str(finding))
    if found==-1:
        return -1
numofcows,num=input().split()
numofcows=int(numofcows)
num=int(num)
count=0
check=1
actual=0
while count<numofcows:
    if finder(check,num)==-1:
        count=count+1
        actual=check
    check=check+1
print(actual)
'''
numoflights,numofcommands=input().split()
numoflights=int(numoflights)
numofcommands=int(numofcommands)
array=[0]*(numoflights+1)
count=0
for i in range(numofcommands):
    command,index1,index2=input().split()
    command=int(command)
    index1=int(index1)
    index2=int(index2)
    if command==0:
        for i in range(index1,index2+1):
            if array[i]==0:
                array[i]=1
            elif array[i]==1:
                array[i]=0
    elif command==1:
        for i in range(index1,index2+1):
            if array[i]==1:
                count=count+1
        print(count)
    count=0