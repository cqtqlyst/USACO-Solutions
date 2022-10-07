'''
x,y=input().split()
x=int(x)
y=int(y)
direction=1
numsteps=1
total=0
if y>x:
    cowonright=1
else:
    cowonright=0
target=x
j=0
b=0
currentpos=x
while j==b:
    target=x+(numsteps*direction)
    if cowonright==1 and direction==1:
        if target>=y:
            total+=y-currentpos
            break
        else:
            total+=target-currentpos
            break
    if cowonright==0 and direction==-1:
        if target<=y:
            total+=abs(cowpos-currentpos)
            break
        else:
            total+=abs(target-currentpos)
            break
    currentpos=target
    direction*=-1
    numsteps*=2
print(total)

numofbeats,numofquestions=input().split()
numofbeats=int(numofbeats)
numofquestions=int(numofquestions)
beats=[0]*numofbeats
for i in range(numofbeats):
    beats[i]=int(input())
questions=[0]*numofquestions
for i in range(numofquestions):
    questions[i]=int(input())
timeline=[0]*10000
total=0
for i in range(numofbeats):
    total+=beats[i]
ctr=0
index=0
for i in range(total):
    ctr+=1
    timeline[i]=index+1
    if ctr==beats[index]:
        ctr=0
        index+=1
for i in range(numofquestions):
    question=questions[i]
    print(timeline[question])
'''
def comp(c):
    return c[0]
numofcoords=int(input())
cows=[0]*numofcoords
for i in range(numofcoords):
    cows[i]=[0]*2
for i in range(numofcoords):
    x,y=input().split()
    x=int(x)
    y=int(y)
    cows[i][0]=x
    cows[i][1]=y
posx=[0]*numofcoords
posy=[0]*numofcoords
for i in range(numofcoords):
    posx[i]=cows[i][0],i
    posy[i]=cows[i][1],i
posx.sort(key=comp)
posy.sort(key=comp)
minx=posx[0][1]
miny=posy[0][1]
maxx=posx[numofcoords-1][1]
maxy=posy[numofcoords-1][1]
elimcow=[0]*4
elimcow[0]=minx
elimcow[1]=miny
elimcow[2]=maxx
elimcow[3]=maxy
minarea=1600000000000000000000001
for i in range(4):
    cownum=elimcow[i]
    minx=40001
    miny=40001
    maxx=0
    maxy=0
    for j in range(numofcoords):
        if j!=cownum:
            minx=min(minx,cows[j][0])
            miny=min(miny,cows[j][1])
            maxx=max(maxx,cows[j][0])
            maxy=max(maxy,cows[j][1])
    area=(maxy-miny)*(maxx-minx)
    minarea=min(minarea,area)
print(minarea)