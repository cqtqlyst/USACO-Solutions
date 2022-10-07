'''
fin=open('breedflip.in','r')
fout=open('breedflip.out','w')
num=int(fin.readline())
correct=fin.readline()
incorrect=fin.readline()
ctr=0
i=0
for i in range(num):
    if incorrect[i]!=correct[i]:
        if incorrect[i+1]==correct[i+1]:
            ctr+=1
ctr=str(ctr)
fout.write(ctr)
fout.close()
'''
fin=open('swap.in','r')
fout=open('swap.out','w')
num,numoftimes=map(int,fin.readline().split())
a1,a2=map(int,fin.readline().split())
b1,b2=map(int,fin.readline().split())
ctr=0
check=True
array=[0]*num
checkarray=[0]*num
for i in range(num):
    array[i]=i+1
    checkarray[i]=i+1
for i in range(numoftimes):
    switchi=a2-1
    i=a1-1
    while switchi>=i:
        a=array[i]
        b=array[switchi]
        array[i]=b
        array[switchi]=a
        switchi-=1
        i+=1
    switchi=b2-1
    i=b1-1
    while switchi>=i:
        a=array[i]
        b=array[switchi]
        array[i]=b
        array[switchi]=a
        switchi-=1
        i+=1
    ctr+=1
    check==True
    for i in range(num):
        if array[i]!=checkarray[i]:
            check=False
    if check==True:
        for i in range(num):
            array[i]=i+1
        for i in range(numoftimes%ctr):
            switchi=a2-1
            i=a1-1
            while switchi>=i:
                a=array[i]
                b=array[switchi]
                array[i]=b
                array[switchi]=a
                switchi-=1
                i+=1
            switchi=b2-1
            i=b1-1
            while switchi>=i:
                a=array[i]
                b=array[switchi]
                array[i]=b
                array[switchi]=a
                switchi-=1
                i+=1
            break
    check=True
for i in range(num):
    fout.write(str(array[i])+"\n")
fout.close()
'''
string=""
for i in range(num):
    string+=str(i+1)
for i in range(numoftimes):
    substring=string[a1-1:a2]
    substring=substring[len(substring)::-1]
    begin=string[:a1-1]
    end=string[a2:]
    string=begin+substring+end
    substring=string[b1-1:b2]
    substring=substring[len(substring)::-1]
    begin=string[:b1-1]
    end=string[b2:]
    string=begin+substring+end

fin=open('triangles.in','r')
fout=open('triangles.out','w')
num=int(fin.readline())
array=[0]*num
for i in range(num):
    array[i]=[0]*2
for i in range(num):
    a,b=map(int,fin.readline().split())
    array[i][0]=a
    array[i][1]=b
maxpos=0
for i in range(num):
    for j in range(num):
        for c in range(num):
            if (array[c][0]==array[j][0] and array[c][1]==array[i][1]) or (array[c][1]==array[j][1] and array[c][0]==array[i][0]):
                x=abs(array[i][0]-array[j][0])
                y=abs(array[i][1]-array[j][1])
                area=x*y
                if area>maxpos:
                    maxpos=area
fout.write(str(maxpos))
fout.close()
'''