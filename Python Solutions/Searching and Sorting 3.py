'''
numofnum,height=input().split()
numofnum=int(numofnum)
height=int(height)
array=[0]*numofnum
for i in range(numofnum):
    array[i]=int(input())
array.sort()
total=0
counter=0
i=0
while total<height:
    total=total+array[i]
    counter=counter+1
    i=i+1

def compabsA(a):
    return abs(a)
numofmin,numofnum=input().split()
numofmin=int(numofmin)
numofnum=int(numofnum)
i=0
prepos=0
current=0
array=[0]*numofnum
for i in range(numofnum):
    array[i]=int(input())
array.sort(key=abs)
while current<numofmin and i<numofnum:
    current=current+(abs(prepos-array[i]))
    prepos=array[i]
    i+=1
print(i-1)

row,col=input().split()
row=int(row)
col=int(col)
matrix=[0]*row
for i in range(row):
    s=input()
    for j in range(col):
        matrix[i][j]=s[j]
counter=0
for r in range(row):
    for c in range(col):
        if matrix[r][c]==".":
            if (c==0 or matrix[r][c-1]=="#") and c<col-2 and (matrix[r][c+1]=="." and matrix[r][c+2]=="."):
                counter=counter+1
                matrix[r][c]="c"
            elif (r==0 or matrix[r-1][c]=="#") and r<row-2 and (matrix[r+1][c]=="." and matrix[r+2][c]=='.'):
                counter=counter+1
                matrix[r][c]="c"
print(counter)
for r in range(row):
    for c in range(col):
        if matrix[r][c]="c":        
            print(r+" "+c)
'''
row,col,numofq=input().split()
row=int(row)
col=int(col)
numofq=int(numofq)
counter=0
matrix=[0]*row
for i in range(row):
    matrix[i]=[0]*col
for i in range(row):
    j=0
    for n in input().split():
        matrix[i][j]=int(n)
        j=j+1
cows=[0]*row
for i in range(numofq):
    que,ans=input().split()
    que=int(que)
    ans=int(ans)
    for r in range(row):
        if matrix[r][que-1]!=ans:
            cows[r]=1
for i in range(row):
    if cows[i]==0:
        counter=counter+1
print(counter)













