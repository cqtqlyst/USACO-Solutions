'''
numofd,difference=input().split()
numofd=int(numofd)
difference=int(difference)
array=[0]*numofd
for i in range(numofd):
    array[i]=int(input())
maxi=0
current=0
for i in range(numofd):
    for j in range(numofd):
        if i!=j:
            if (abs(array[i]-array[j]))<=difference:
                current=current+1
    if current>maxi:
        maxi=current
    current=0
print(maxi)

row,col=input().split()
row=int(row)
col=int(col)
matrix=[0]*row
for i in range(row):
    matrix[i]=[0]*col
for i in range(row):
    s=input()
    for k in range(len(s)):
        matrix[i][k]=s[k]
counter=0
for i in range(row):
    for k in range(col):
        if matrix[i][k]=="#":
            counter=counter+1
            if i!=row-1:
                if matrix[i+1][k]=="#":
                    matrix[i+1][k]="."
            if k!=col-1:    
                if matrix[i][k+1]=="#":
                    matrix[i][k+1]="."
print(counter)
'''          
check=0
n=0
counter=0
num=int(input())
matrix=[0]*num
for i in range(num):
    matrix[i]=0*num
for i in range(num):
    s=input()
    for j in range(num):
        matrix[i][j]=s[j]
while n==0:
    check=0
    for r in range(num,-1,-1):
        for c in range(num,-1,-1):
            if matrix[r][c]=="1":
                counter=counter+1
                for i in range(r):
                    for j in range(c):
                        if matrix[r][c]=="1":
                            matrix[r][c]="0"
                        if matrix[r][c]=="0":
                            matrix[r][c]="1"
    for a in range(num):
        for b in range(num):
            if matrix[a][b]=="0":
                check=check+1
    if check==num**2:
        break
print(counter)
            
            
            
            
            
            