n=int(input())
array=[0]*n
stopped=[0]*n
enum=[]
ex=[]
ey=[]
nx=[]
ny=[]
nnum=[]
for i in range(n):
    stopped[i]=0,[]
for i in range(n):
    c,x,y=input().split()
    x=int(x)
    y=int(y)
    array[i]=c,x,y,i
    if c=="E":
        ex.append(x)
        ey.append(y)
        enum.append(i)
    else:
        nx.append(x)
        ny.append(y)
        nnum.append(i)
#east stops north
for i in range(len(ex)):
    for j in range(len(nx)):
        if ex[i]<=nx[j] and ey[i]>ny[j] and abs(ex[i]-nx[j])<abs(ey[i]-ny[i]):
            stopped[enum[i]][0]+=1
            stopped[enum[i]][1].append(nnum[j])
#north stops east
for i in range(len(ex)):
    for j in range(len(nx)):
        if ex[i]<nx[j] and ey[i]>=ny[j] and abs(ex[i]-nx[j])>abs(ey[i]-ny[i]):
            stopped[nnum[j]][0]+=1
            stopped[nnum[j]][1].append(enum[i])
for i in range(n):
    for j in range(len(stopped[i][1])):
        stopped[i][0]+=stopped[stopped[i][1][j]][0]
for i in range(n):
    print(stopped[i][0])
    