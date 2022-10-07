r,c=input().split()
r=int(r)
c=int(c)
array=[0]*c
matrix=[0]*r
for i in range(r):
    matrix[i]=[0]*c
for i in range(r):
    string=input()
    for k in range(c):
        matrix[i][k]=string[k]
        if matrix[i][k]=="C":
            rstart=i
            cstart=k
ix=[0,1,0,-1]
iy=[1,0,-1,0]
visited=[0]*r
for i in range(r):
    visited[i]=[0]*c
qrow=[]
qcol=[]
qmoves=[]
visited[rstart][cstart]=1
qrow.append(rstart)
qcol.append(cstart)
qmoves.append(0)
x=0
while len(qrow)>0:
    currentr=qrow.pop(0)
    currentc=qcol.pop(0)
    distance=qmoves.pop(0)
    for i in range(4):
        if currentr+ix[i]<r and currentr+ix[i]>-1 and currentc+iy[i]<c and currentc+iy[i]>-1: 
            if matrix[currentr+ix[i]][currentc+iy[i]]=="." and visited[currentr+ix[i]][currentc+iy[i]]==0:
                qrow.append(currentr+ix[i])
                qcol.append(currentc+iy[i])
                qmoves.append(distance+1)
                visited[currentr+ix[i]][currentc+iy[i]]=1
            if matrix[currentr+ix[i]][currentc+iy[i]]=="B":
                x=1
                print(distance+1)
                break
    if x==1:
        break