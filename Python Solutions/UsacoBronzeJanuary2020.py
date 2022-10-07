'''
fin=open('word.in','r')
fout=open('word.out','w')
num,numofcharac=map(int, fin.readline().split())
array=[0]*num
array=fin.readline().split()
ctr=0
ncleft=numofcharac
while ctr<num:
    if len(array[ctr])<=ncleft:
        ncleft=ncleft-len(array[ctr])
        if ctr+1==num:
            fout.write(array[ctr])
        elif len(array[ctr+1])>ncleft:
            fout.write(array[ctr]+"\n")
            ncleft=numofcharac
        elif len(array[ctr+1])<=ncleft:
            fout.write(array[ctr]+" ")
        ctr+=1    
    elif len(array[ctr])>ncleft:
        fout.write(array[ctr]+" ")
        ctr=ctr+1
        ncleft=numofcharac
fout.close()

fin=open('photo.in','r')
fout=open('photo.out','w')
num=int(fin.readline())
newnum=num-1
array=[0]*(newnum)
array=fin.readline().split()
for i in range(newnum):
    array[i]=int(array[i])
numbers=[0]*num
actual=newnum-1
for i in range(newnum):
    numbers[i]=actual
    actual=array[i]-actual
numbers[num-1]=actual
for i in range(newnum):
    fout.write(str(numbers[i])+' ')
fout.write(str(numbers[num-1]))
fout.close()

fin=open('race.in','r')
fout=open('race.out','w')
distance,numoflines=map(int, fin.readline().split())
for i in range(numoflines):
    num=int(fin.readline())
    speed=0
    currentdistance=0
    ctr=0
    total=0
    j=0
    while ctr<distance:
        speed+=1
        total=0
        if j==1:
            break
        currentdistance+=speed
        distanceleft=distance-currentdistance
        ctr+=1
        if speed<num:
            for a in range(speed,num):
                total+=a
            if total+currentdistance>=distance:
                ctr+=(abs(speed-num))
                if (total+currentdistance)-distance>=speed:
                    x=int(((total+currentdistance)-distance)/speed)
                    ctr=ctr-x
                fout.write(str(ctr)+"\n")
                j=1
        elif speed>=num:
            for a in range(num,speed):
                total+=a
            if total+currentdistance>=distance:
                ctr+=(abs(speed-num))
                if (total+currentdistance)-distance>=speed:
                    x=int(((total+currentdistance)-distance)/speed)
                    ctr=ctr-x
                fout.write(str(ctr)+"\n")
                j=1
fout.close()
'''
fin=open('photo.in','r')
fout=open('photo.out','w')
num=int(fin.readline())
b=[0]*num
b=fin.readline().split()
for i in range(num):
    b[i]=int(b[i])
a=[0]*num
for i in range(1,b[0])
    a=[0]*num
    a[0]=i
    wrong=False
    for j in range(num-1):
        a[j+1]=b[j]-a[j]
        if a[j+1]<=0 or a[j+1]>num:
            wrong=True
        for k in range(num):
            if a[j+1]==a[k]
                wrong=True
        if wrong==True:
            break
    if wrong==False:
        break
for i in range
fout.close()





