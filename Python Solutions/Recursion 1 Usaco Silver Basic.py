'''
def fact(x):
    if x==1:
        return 1
    return x*fact(x-1)
n=int(input())
print(fact(n))

def fib(x):
    if x==1 or x==2:
        return 1
    return fib(x-1)+fib(x-2)
n=int(input())
print(fib(n))

def ruler(x):
    if x==1:
        print("*")
        return ""
    else:
        ruler(x-1)
        for i in range(x):
            print("*",end="")
        print()
        ruler(x-1)
n=int(input())
for i in range(n):
    print("*",end="")
print()
ruler(n-1)
for i in range(n):
    print("*",end="")

def numgen(x):
    global n
    global number
    global array
    if x==n:
        process()
        return
    for i in range(m):
        number[x]=array[i]
        numgen(x+1)
def process():
    value=0
    for i in range(n):
        value=value*10+number[i]
    print(value)
m=int(input())
array=[0]*m
array=[int(i) for i in input().split()]
n=int(input())
number=[0]*n
numgen(0)

def permgen(e):
    global used
    global n
    global number
    if e==n:
        process()
        return
    for i in range(m):
        if used[i]==0:
            used[i]=1
            number[e]=array[i]
            permgen(e+1)
            used[i]=0
def process():
    value=0
    for i in range(n):
        value=value*10+number[i]
    print(value)
m=int(input())
array=[0]*m
array=[int(i) for i in input().split()]
n=int(input())
number=[0]*n
used=[0]*m
permgen(0)

def combogen(e,cnt):
    global elements
    global number
    global m
    global n
    global array
    if e==m and cnt==n:
        process()
        return
    elif e==m and cnt!=n:
        return
    else:
        elements[e]=1
        combogen(e+1,cnt+1)
        elements[e]=0
        combogen(e+1,cnt)
def process():
    value=0
    for i in range(m):
        if elements[i]==1:
            value=value*10+array[i]
    print(value)
m=int(input())
array=[0]*m
array=[int(i) for i in input().split()]
n=int(input())
elements=[0]*m
combogen(0,0)

def combogen(e,cnt):
    global elements
    global number
    global m
    global n
    global array
    if e==m and cnt==n:
        process()
        return
    elif e==m and cnt!=n:
        return
    else:
        elements[e]=1
        combogen(e+1,cnt+1)
        elements[e]=0
        combogen(e+1,cnt)
def process():
    value=0
    for i in range(m):
        if elements[i]==1:
            value=value*10+array[i]
    print(value)
m=int(input())
array=[0]*m
array=[int(i) for i in input().split()]
elements=[0]*m
for n in range(1,m+1):
    combogen(0,0)
'''
