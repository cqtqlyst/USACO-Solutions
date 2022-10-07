'''
numofcol,numofrow,numoflines=input().split()
numofcol=int(numofcol)
numofrow=int(numofrow)
numoflines=int(numoflines)
matrix=[0]*numofrow
for i in range(numofrow):
    matrix[i]=[0]*numofcol
counter=0
for i in range(numoflines):
    xll,yll,xur,yur=input().split()
    xll=(int(xll))-1
    yll=(int(yll))-1
    xur=(int(xur))-1
    yur=(int(yur))-1
    cs=xll-1
    cf=xur
    rf=yur
    rs=yll-1
    for row in range(rs,rf):
        for col in range(cs,cf):
            matrix[row][col]=1
for i in range(numofrow):
    for j in range(numofcol):
        if matrix[i][j]==1:
            counter=counter+1
print(counter)

num=int(input())
array=[0]*num
array=[int(i) for i in input().split()]
array.sort()
counter=0
passtoright=[0]*num
passtoright[num-1]=1
for i in range(1,num-1):
    if abs(array[i-1]-array[i])>=abs(array[i+1]-array[i]):
        passtoright[i]=1
    else:
        passtoright[i]=0
recball=[0]*num
for i in range(1,num-1):
    if passtoright[i-1]==0:
        recball[i]+=1
    if passtoright[i+1]==1:
        recball[i]+=1
for i in range(num):
    if recball[i]==0:
        counter+=1
for i in range(num):
    if recball[i]==1 and recball[i+1]==1 and passtoright[i]==0 and passtoright[i+1]==1:
        counter+=1
print(counter)
'''   
    
    
    
    
    