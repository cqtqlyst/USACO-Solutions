'''
def funcInd(let):
    for i in range(3):
        if m[i][0]==let and m[i][1]==let and m[i][2]==let:
            return True
    for i in range(3):
        if m[0][i]==let and m[1][i]==let and m[2][i]==let:
            return True
    if m[0][0]==let and m[1][1]==let and m[2][2]==let:
        return True
    if m[2][0]==let and m[1][1]==let and m[0][2]==let:
        return True
def funcTeam(let1,let2):
    for i in range(3):
        if(m[i][0]==let1 or m[i][0]==let2) and (m[i][1]==let1 or m[i][1]==let2) and (m[i][2]==let1 or m[i][2]==let2) and (m[i][0]!=m[i][1] or m[i][1]!=m[i][2]):
            return True
    for i in range(3):
        if(m[0][i]==let1 or m[0][i]==let2) and (m[1][i]==let1 or m[1][i]==let2) and (m[2][i]==let1 or m[2][i]==let2) and (m[0][i]!=m[1][i] or m[1][i]!=m[2][i]):
            return True
    if (m[0][0]==let1 or m[0][0]==let2) and (m[1][1]==let1 or m[1][1]==let2) and (m[2][2]==let1 or m[2][2]==let2) and (m[0][0]!=m[1][1] or m[1][1]!=m[2][2]):
        return True
    if (m[2][0]==let1 or m[2][0]==let2) and (m[1][1]==let1 or m[1][1]==let2) and (m[0][2]==let1 or m[0][2]==let2) and (m[2][0]!=m[1][1] or m[1][1]!=m[0][2]):
        return True    
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m=[0]*3
for i in range(3):
    m[i]=[0]*3
for i in range(3):
    string=input()
    for j in range(3):
        m[i][j]=string[j]
indCounter=0
for i in range(26):
    letter=alphabet[i]
    if funcInd(letter)==True:
        indCounter+=1
teamCounter=0
for i in range(26):
    letter1=alphabet[i]
    for j in range(i+1,26):
        letter2=alphabet[j]
        if funcTeam(letter1,letter2)==True:
            teamCounter+=1
'''
n=int(input())
m=[0]*n
for i in range(n):
    m[i]=[0]*n
visible=[0]*10
rs=[n]*10
re=[-1]*10
cs=[n]*10
ce=[-1]*10
isPainted=[0]*10
for r in range(n):
    s=input()
    for c in range(n):
        m[r][c]=int(s[c])
        char=int(s[c])
        if char!=0:
            rs[char]=min(rs[char],r)
            re[char]=max(re[char],r)
            cs[char]=min(cs[char],c)
            ce[char]=max(ce[char],c)
            visible[char]=1
            isPainted[char]=1
for color in range(1,10):
    if visible[color]==1:
        for r in range(rs[color],re[color]+1):
            for c in range(cs[color],ce[color]+1):
                current=m[r][c]
                if current!=color:
                    isPainted[current]=0
total=0
for i in range(1,10):
    if isPainted[i]==1:
        total+=1
print(total)
            
        