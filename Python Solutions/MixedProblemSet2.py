'''
def funct(b,e,s,i,g,o,m):
    return ((b+2*e+2*s+i)*(g+o+e+s)*(m+2*0))
myletter="BESIGOM"
num=int(input())
arr=[0]*7
counter=0
for i in range(7):
    arr[i]=[0]*2
for i in range(num):
    letter,value=input().split()
    value=int(value)
    for i in range(7):
        if myletter[i]==letter:
            if value%2==0:
                arr[i][1]+=1
            else:
                arr[i][0]+=1
for b in range(2):
    for e in range(2):
        for s in range(2):
            for i in range(2):
                for g in range(2):
                    for o in range(2):
                        for m in range(2):
                            if funct(b,e,s,i,g,o,m)%2==0:
                                temp=1
                                if b==0:
                                    temp*=arr[0][1]
                                else:
                                    temp*=arr[0][0]
                                if e==0:
                                    temp*=arr[1][1]
                                else:
                                    temp*=arr[1][0]
                                if s==0:
                                    temp*=arr[2][1]
                                else:
                                    temp*=arr[2][0]
                                if i==0:
                                    temp*=arr[3][1]
                                else:
                                    temp*=arr[3][0]
                                if g==0:
                                    temp*=arr[4][1]
                                else:
                                    temp*=arr[4][0]
                                if o==0:
                                    temp*=arr[5][1]
                                else:
                                    temp*=arr[5][0]
                                if m==0:
                                    temp*=arr[6][1]
                                else:
                                    temp*=arr[6][0]
                                counter+=temp
print(counter)

numofcows,num=input().split()
numofcows=int(numofcows)
num=int(num)
start=[0]*numofcows
cowinfo=[0]*numofcows
for i in range(num):
    cownum,check,hour,minute=input().split()
    cownum=int(cownum)
    hour=int(hour)
    minute=int(minute)
    total=(hour*60)+minute
    if check=="START":
        start[cownum-1]=total               
    if check=="STOP":
        cowinfo[cownum-1]+=total-start[cownum-1]
for i in range(numofcows):
    hour=cowinfo[i]//60
    minute=cowinfo[i]%60
    print(hour,minute)

def sort(a):
    return a[0]
num=int(input())
array=[0]*num
for i in range(num):
    time,qtime=input().split()
    time=int(time)
    qtime=int(qtime)
    array[i]=time,qtime
array.sort(key=sort)
current=0
for i in range(num):
    s=array[i][0]
    d=array[i][1]
    if current<s:
        current=s
    current+=d
print(current)
'''
def funct90(n,array):
    change=[0]*n
    for i in range(n):
        change[i]=[0]*n
    for r in range(n):
        for c in range(n):
            change[c][n-r-1]=array[r][c]
    return change
def ref(n,array):
    change=[0]*n
    for i in range(n):
        change[i]=[0]*n
    for r in range(n):
        for c in range(n):
            change[r][r-1-c]=array[r][c]
    return change
n=int(input())
orig=[0]*n
change=[0]*n
for i in range(n):
    orig[i]=[0]*n
    change=[0]*n
for i in range(n):
    orig[i]=[j for j in input().split()]
for i in range(n):
    change[i]=[j for j in input().split()]
if funct90(n,orig)==change:
    print(1)
elif funct90(funct90(n,orig))==change:
    print(2)
elif funct90(funct90(funct90(n,orig)))==change:
    print(3)
elif ref(n,orig)==change:
    print(4)
elif funct90(ref(n,orig))==change:
    print(5)
elif funct90(funct90(ref(n,orig)))==change:
    print(5)
elif funct90(funct90(funct90(ref(n,orig))))==change:
    print(5)
elif orig==change:
    print(6)
else:
    print(7)