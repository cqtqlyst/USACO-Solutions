n=int(input())
matrix=[0]*100
for i in range(100):
    matrix[i]=[0]*100
array=[0]*n
array1=[0]*n
array2=[0]*n
array3=[0]*n
array4=[0]*n
array5=[0]*n
count=[0]*n
for i in range(n):
    c,x,y=input().split()
    x=int(x)
    y=int(y)
    valid=0
    diedto=-1
    array[i]=c,x,y,valid,i,diedto
    array1[i]=x
    array2[i]=y
    array3[i]=valid
    array4[i]=i
    array5[i]=diedto
for j in range(100):
    for i in range(n):
        if array[i][3]==0:
            if array[i][0]=="E":
                array2[i]+=1
                matrix[x][y]=array4[i]
                if matrix[array1[i]][array2[i]]>0:
                    array5[i]==matrix[array1[i]][array2[i]]
                    array4[i]=1
            if array[i][0]=="N":
                array3[i]+=1
                matrix[x][y]=array4[i]
                if matrix[array1[i]][array2[i]]>0:
                    array5[i]=matrix[array1[i]][array2[i]]
                    array3[i]=1
for i in range(n):
    sumi=0
    for j in range(n):
        if array5[j]==i:
            sumi+=1
    count[i]=sumi
for i in range(n):
    print(count[i])