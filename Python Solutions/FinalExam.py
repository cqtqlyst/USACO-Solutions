'''
x,y,z,w=input().split()
x=int(x)
y=int(y)
z=int(z)
w=int(w)
actual=min(x,y,z,w)
print(actual)

x=int(input())
for i in range(x):
    print("O-O",end=" ")

count=0
numofnum=int(input())
for i in range(numofnum):
    x=int(input())
    if x==7:
        count=count+1
print(count)

num=int(input())
last=num
current=0
for i in range(num):
    current=int(input())
    if current>last:
        print(current)
        last=current

character=input()
numofstrings=int(input())
count=0
for i in range(numofstrings):
    string=input()
    size=len(string)
    for x in range(size):
        if string[x]==character:
            count=count+1
print(count)

num=int(input())
for i in range(1,num+1):
    for x in range(1,i+1):
        print(i-x+1,end="")
    print("")
'''
string=list(input())
original=string
size=len(string)
current=string
for i in range(size):
    string[i]=int(string[i])
    current[i]=int(current[i])
for i in range(size):
    if current[i]==0:
        current[i]=1
    elif current[i]==1:
        current[i]=0
    print(current)
    #for a in range(size):
    #    print(current[a],end="")
    #print("")
    for x in range(i,i+1):
        if current[x]==1:
            current[x]=0
        elif current[x]==0:
            current[x]=1
    print(current)
'''
row,column=input().split()
row=int(row)
column=int(column)
matrix=[0]*row
for i in range(row):
    matrix[i]=[0]*column
for i in range(row):
    matrix[i]=input().split()
    for x in range(column):
        matrix[i][x]=int(matrix[i][x])
for i in range(row):
    for y in range(2):
        for x in range(column):
            print(matrix[i][x],end=" ")
    print("")

x=int(input())
for i in range(1,4):
    if i==1:
        x=((x**3)-(4*x)+17)%1000
    if i==2:
        x=((-2*(x**2))+(5*x)-1)%1000
    if i==3:
        x=((3*(x**2))-(7*x)+3)%1000
for i in range(2,0,-1):    
    if i==1:
        x=((x**3)-(4*x)+17)%1000
    if i==2:
        x=((-2*(x**2))+(5*x)-1)%1000
for i in range(2,4):
    if i==2:
        x=((-2*(x**2))+(5*x)-1)%1000
    if i==3:
        x=((3*(x**2))-(7*x)+3)%1000    
print(x)

row,column=input().split()
row=int(row)
column=int(column)
matrix=[""]*row
for i in range(row):
    matrix[i]=[""]*column
for i in range(row):
    matrix[i]=list(input())
for i in range(row):
    for x in range(column):
        if matrix[i][x]=="S":
            playerrow=i
            playercol=x
matrix[playerrow][playercol]="P"
path=input()
size=len(path)
yn=0
numofmoves=0
for i in range(size):
    print("Your move: "+path[i])
    if path[i]=="R":
        playercol=playercol+1
        if matrix[playerrow][playercol]=="#":
            print("Invalid move!")
            playercol=playercol-1
            numofmoves=numofmoves-1
        elif matrix[playerrow][playercol]==".":
            matrix[playerrow][playercol]="P"
            matrix[playerrow][playercol-1]="."
        else:
            yn=1
            matrix[playerrow][playercol]="P"
            matrix[playerrow][playercol-1]="."            
    elif path[i]=="L":
        playercol=playercol-1
        if matrix[playerrow][playercol]=="#":
            print("Invalid move!")
            playercol=playercol+1
            numofmoves=numofmoves-1
        elif matrix[playerrow][playercol]==".":
            matrix[playerrow][playercol]="P"
            matrix[playerrow][playercol+1]="."
        else:
            yn=1
            matrix[playerrow][playercol]="P"
            matrix[playerrow][playercol+1]="."
    elif path[i]=="D":
        playerrow=playerrow+1
        if matrix[playerrow][playercol]=="#":
            print("Invalid move!")
            playerrow=playerrow-1
            numofmoves=numofmoves-1
        elif matrix[playerrow][playercol]==".":
            matrix[playerrow][playercol]="P"
            matrix[playerrow-1][playercol]="."
        else:
            yn=1
            matrix[playerrow][playercol]="P"
            matrix[playerrow-1][playercol]="."
    else:
        playerrow=playerrow-1
        if matrix[playerrow][playercol]=="#":
            print("Invalid move!")
            playerrow=playerrow+1
            numofmoves=numofmoves-1
        elif matrix[playerrow][playercol]==".":
            matrix[playerrow][playercol]="P"
            matrix[playerrow+1][playercol]="."
        else:
            yn=1
            matrix[playerrow][playercol]="P"
            matrix[playerrow+1][playercol]="."
    numofmoves=numofmoves+1
    print("Number of moves: "+str(numofmoves))
    for i in range(row):
        for x in range(column):
            print(matrix[i][x],end="")
        print("")
    print("")
    if yn==1:
        break
if yn==1:
    print("Congratulations you found the exit!")
'''