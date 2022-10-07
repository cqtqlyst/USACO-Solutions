'''
n,b=input().split()
n=int(n)
b=int(b)
array=[0]*n
for i in range(n):
    array[i]=int(input())
ans=100000000000000000000000000000
array.sort()
for mask in range(1<<n):
    sume=0
    for i in range(n):
        if ((1<<i) & mask)>0:
            sume+=array[i]
    if sume>=b:
        ans=min(ans,sume-b)
print(ans)
'''
def solve():
    def comp(c):
        return c[0]
    n=int(input())
    array=[0]*n
    for i in range(n):
        w,b=input().split()
        w=int(w)
        b=int(b)
        array[i]=w,b
    array.sort(key=comp)
    for mask in range(2**n):
        ok=True
        prevbreadth=-1
        if ((1<<i) & mask)>0:
            if array[i][1]<prevbreadth:
                ok=False
            prevbreadth=breadth[i]
    if ok:
        s=str(mask)
        count=0
        for i in range(len(s)):
            if s[i]=="1":
                count+=1
        ans=max(ans,count)
solve()