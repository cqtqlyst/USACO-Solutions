'''
n=int(input())
array=[0]*n
for i in range(n-1):
    a,b=input().split()
    a=int(a)
    b=int(b)
    array[a-1]+=1
    array[b-1]+=1
maxi=0
for i in range(n):
    if array[i]>maxi:
        maxi=array[i]
print(maxi+1)

p,ns,t=input().split()
p=int(p)
ns=int(ns)
t=int(t)
parent=[0]*(p+1)
for i in range(ns):
    n,b1,b2=input().split()
    n=int(n)
    b1=int(b1)
    b2=int(b2)
    parent[b1]=n
    parent[b2]=n
current=t
l=[]
while True:
    l.append(current)
    current=parent[current]
    if current==1:
        l.append(current)
        break
print(len(l))
for i in range(len(l)):
    print(l[len(l)-i-1])

def dfs(curnode):
    global vis
    vis[curnode]=1
    for newnode in range(1,n+1):
        if array[curnode][newnode]==1 and vis[newnode]==0:
            dfs(newnode)
n,m=input().split()
n=int(n)
m=int(m)
array=[0]*(n+1)
for i in range(n+1):
    array[i]=[0]*(n+1)
for i in range(m):
    c1,c2=input().split()
    c1=int(c1)
    c2=int(c2)
    array[c1][c2]=1
    array[c2][c1]=1
vis=[0]*(n+1)
dfs(1)
yes=True
for i in range(1,n+1):
    if vis[i]==0:
        yes=False
        print(i)
if yes==True:
    print(0)
'''
def dfs(curnode,dist):
    global p2
    global curans
    global vis
    global array
    if curnode==p2:
        curans=dist
    vis[curnode]=1
    for i in range(len(array[curnode])):
        newnode=array[curnode][i][0]
        weight=array[curnode][i][1]
        if vis[newnode]==0:
            dfs(newnode,dist+weight)
n,q=input().split()
n=int(n)
q=int(q)
array=[[]]*(n+1)
vis=[0]*(n+1)
curans=0
for i in range(n-1):
    u,v,w=input().split()
    u=int(u)
    v=int(v)
    w=int(w)
    arr=[0]*2
    arr[0]=v
    arr[1]=w
    array[u].append(arr)
    arr[0]=u
    array[v].append(arr)
for i in range(q):
    p1,p2=input().split()
    p1=int(p1)
    p2=int(p2)
    dfs(p1,0)
    print(curans)
    vis=[0]*n
    curans=0