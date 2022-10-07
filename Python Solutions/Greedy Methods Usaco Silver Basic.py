'''
def check(x):
    curint=0
    loc=intervals[0][0]
    for i in range(1,n):
        loc+=x
        while curint<m and intervals[curint][1]<loc:
            curint+=1
        if curint==m:
            return False
        if loc<intervals[curint][0]:
            loc=intervals[curint][0]
    return True
def bs():
    global maxi
    l=0
    r=maxit+1
    mid=(l+r)//2
    while l+1<r:
        mid=(l+r)//2
        if check(mid)==True:
            maxi=max(mid,maxi)
            l=mid
        else:
            r=mid
    return True     
def comp(c):
    return c[0]
n,m=input().split()
n=int(n)
m=int(m)
maxit=0
intervals=[0]*m
maxi=0
for i in range(m):
    a,b=input().split()
    a=int(a)
    b=int(b)
    maxit=max(maxit,a)
    maxit=max(maxit,b)
    intervals[i]=a,b
intervals.sort(key=comp)
bs()
print(maxi)
'''
def comp(c):
    return c[2]
n=int(input())
array=[0]*n
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    l=a-b
    r=a+b
    array=a,b,l,r
array.sort(key=comp)
righti=0
counter=0
for i in range(n):
    if array[i][3]>array[righti][3]:
        righti=i
    if array[i][3]<array[righti][3] and array[i][2]>array[righti][2]:
        counter+=1
print(counter)