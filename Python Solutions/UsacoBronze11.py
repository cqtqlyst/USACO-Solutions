'''
numofrows,startnum=input().split()
numofrows=int(numofrows)
startnum=int(startnum)
count=startnum
matrix=[""]*numofrows
for i in range(numofrows):
    matrix[i]=[" "]*numofrows
for i in range(numofrows):
    for x in range(i+1):
        matrix[x][i]=count
        count=count+1
        if count==10:
            count=1
for i in range(numofrows):
    for x in range(numofrows):
        print(matrix[i][x],end=" ")
    print("")
'''
columns,rows,numoftimes=input().split()
columns=int(columns)
rows=int(rows)
numoftimes=int(numoftimes)
matrix=["."]*rows
for i in range(rows):
    matrix[i]=["."]*columns
for i in range(numoftimes):
    x1,y1,x2,y2=input().split()
    x1=int(x1)-1
    x2=int(x2)-1
    y1=int(y1)-1
    y2=int(y2)-1
    for x in range(y1,y2+1):
        for a in range(x1,x2+1):
            matrix[x][a]="*"
count=0
for i in range(rows):
    for x in range(columns):
        if matrix[i][x]=="*":
            count=count+1
print(count)


