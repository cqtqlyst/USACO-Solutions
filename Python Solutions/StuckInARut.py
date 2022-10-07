n=int(input())
array=[0]*n
stopped=[0]*n
stopped2=[0]*n
stopped3=[0]*n
stopped4=[0]*n
stopped5=[0]*n
enum=[]
ex=[]
ey=[]
nx=[]
ny=[]
nnum=[]
for i in range(n):
    stopped2[i]=[]
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
        if ex[i]<=nx[j] and ey[i]>ny[j] and abs(ex[i]-nx[j])<abs(ey[i]-ny[j]):
            if stopped4[nnum[j]]==0:
                stopped4[nnum[j]]=1
                stopped[enum[i]]+=1
                stopped2[enum[i]].append(nnum[j])
                stopped3[nnum[j]]=enum[i]
                stopped5[nnum[j]]=((abs(ex[i]-nx[j]))**2)+((abs(ey[i]-ny[j]))**2)
            else:
                if stopped5[nnum[j]]>((abs(ex[i]-nx[j]))**2)+((abs(ey[i]-ny[j]))**2):
                    stopped[stopped3[nnum[j]]]-=1
                    stopped2[stopped3[nnum[j]]].remove(nnum[j])
                    stopped5[nnum[j]]=((abs(ex[i]-nx[j]))**2)+((abs(ey[i]-ny[j]))**2)
                    stopped3[nnum[j]]=enum[i]
                    stopped[enum[i]]+=1
#north stops east
for i in range(len(ex)):
    for j in range(len(nx)):
        if ex[i]<nx[j] and ey[i]>=ny[j] and abs(ex[i]-nx[j])>abs(ey[i]-ny[j]):
            if stopped4[enum[i]]==0:
                stopped[nnum[j]]+=1
                stopped2[nnum[j]].append(enum[i])
                stopped4[enum[i]]=1
                stopped3[enum[i]]=nnum[j]
                stopped5[enum[i]]=((abs(ex[i]-nx[j]))**2)+((abs(ey[i]-ny[j]))**2)
            else:
                if stopped5[enum[i]]>((abs(ex[i]-nx[j]))**2)+((abs(ey[i]-ny[j]))**2):
                    stopped[stopped3[enum[i]]]-=1
                    stopped2[stopped3[enum[i]]].remove(enum[i])
                    stopped5[enum[i]]=((abs(ex[i]-nx[j]))**2)+((abs(ey[i]-ny[j]))**2)
                    stopped3[enum[i]]=enum[i]
                    stopped[nnum[j]]+=1
for i in range(n):
    for j in range(len(stopped2[i])):
        stopped[i]+=stopped[stopped2[i][j]]
for i in range(n):
    print(stopped[i])
    
