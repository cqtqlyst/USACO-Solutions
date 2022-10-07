'''
n=int(input())
field=[[]]*2001
#can also use field=[0]*2001
for i in range(2001):
    field[i]=[0]*2001
row=1000
col=1000
currenttime=0
minofdif=2001
check=False
for i in range(n):
    direction,steps=input().split()
    steps=int(steps)
    for j in range(steps):
        currenttime+=1
        if direction=="N":
            row-=1
        if direction=="E":
            col+=1
        if direction=="S":
            row+=1
        if direction=="W":
            col-=1
        if field[row][col]>0:
            dif=currenttime-field[row][col]
            if dif<minofdif:
                minofdif=dif
            check=True
        field[row][col]=currenttime
if check==False:
    print(-1)
else:
    print(minofdif)
'''
def check(partno,row,col):
    if row<0 or row>n-1 or col<0 or col>n-1:
        return False
    return parts[partno][row][col]
n,numofbroken=input().split()
n=int(n)
numofbroken=int(n)
parts=[0]*(numofbroken+1)
for i in range(numofbroken+1):
    matrix=[0]*n
    for j in range(n):
        matrix[j]=[0]*n
    parts[i]=matrix
for i in range(numofbroken+1):
    for j in range(n):
        s=input()
        for a in range(n):
            if s[a]==".":
                parts[i][j][a]=False
            else:
                parts[i][j][a]=True
x=1
breaker=0
for part1 in range(1,k+1):
    for part2 in range(part1+1,k+1):
        for rp1 in range(-n,n):
            for cp1 in range(-n,n):
                for rp2 in range(-n,n):
                    for cp2 in range(-n,n):
                        found=True
                        for rorg in range(n):
                            for corg in range(n):
                                if parts[0][rorg][corg]==False:
                                    if check(part1,rp1+rorg,cp1+corg)==False or check(part2,rp2+rorg,cp2+corg)==False:
                                        x=1
                                    else:
                                        if parts[part1][rp1+rorg][cp1+corg]==False and parts[part2][rp2+rorg][cp2+corg]==False:
                                            found=True
                                        else:
                                            found=False
                                            breaker=1
                                            break
                                if parts[0][rorg][corg]==True:
                                    if check(part1,rp1+rorg,cp1+corg)==False or check(part2,rp2+rorg,cp2+corg)==False:
                                        x=1
                                    else:
                                        if (parts[part1][rp1+rorg][cp1+corg]==True and parts[part2][rp2+rorg][cp2+corg]==False) or (parts[part1][rp1+rorg][cp1+corg]==False and parts[part2][rp2+rorg][cp2+corg]==True):
                                            found=True
                                        else:
                                            found=False:
                                            breaker=1
                                            break
                            if breaker==1:
                                break
                        if found==True:
                            print(part1,part2)
                                        
                                    
                                
                                    
                        
            