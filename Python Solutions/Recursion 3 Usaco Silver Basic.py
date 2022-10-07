'''
def pathcount(e):
    global counter
    global n
    global string
    if e==(n-1):
        counter+=1
        return
    if e>(n-1):
        return
    for t in range(1,3):
        newloc=e+t
        if newloc>n-1:
            return
        else:
            if string[newloc]=="-":
                pathcount(newloc)
string=input()
n=len(string)
counter=0
pathcount(0)
print(counter)

def subset(e):
    global g
    global elements
    if e==g:
        process()
        return
    elements[e]=1
    subset(e+1)
    elements[e]=0
    subset(e+1)
def process():
    global v
    global g
    global elements
    global req
    global best
    global scoop
    amounts=[0]*v
    current=[]
    for i in range(g):
        if elements[i]==1:
            current.append(i)
            for j in range(v):
                amounts[j]+=scoop[i][j]
    ok=True
    for j in range(v):
        if amounts[j]<req[j]:
            ok=False
    if ok==False:
        return
    if len(best)==0:
        best=current
        return
    if len(best)<len(current):
        return
    if len(current)<len(best):
        best=current
        return
    for i in range(len(best)):
        if best[i]<current[i]:
            return
        if current[i]<best[i]:
            best=current
            return
v=int(input())
req=[0]*v
req=[int(i) for i in input().split()]
g=int(input())
scoop=[0]*g
for i in range(g):
    scoop[i]=[0]*v
for i in range(g):
    scoop[i]=[int(j) for j in input().split()]
elements=[0]*g
best=[]
subset(0)
print(len(best),end=" ")
for i in range(len(best)):
    print(best[i]+1,end=" ")
'''
def combogen2(e,cnt):
    global l
    global c
    global chosen
    if cnt==l:
        process()
        return
    if e==c and cnt<l:
        return
    for i in range(e,c):
        chosen[i]=1
        combogen2(i+1,cnt+1)
        chosen[i]=0
def process():
    global c
    global l
    global letters
    global chosen
    vowelcount=0
    for i in range(c):
        if chosen[i]==1 and isvowel(letters[i])==True:
            vowelcount+=1
def isvowel(c):
    vowels="aeiou"
    for i in range(5):
        if c==vowels[i]:
            return True
    return False
l,c=input().split()
l=int(l)
c=int(c)
chosen=[0]*c
letters=[0]*c
letters=[i for i in input().split()]
letters.sort()
