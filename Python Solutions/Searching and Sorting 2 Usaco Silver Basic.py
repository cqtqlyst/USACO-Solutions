'''
def comp(a,b):
    if a[2]<b[2]:
        return -10
    elif b[2]<a[2]:
        return 10
    elif a[2]==b[2] and a[0]<b[0]:
        return 10
    elif a[2]==b[2] and b[0]<a[0]:
        return -10
    elif a[2]==b[2] and a[1]<b[1]:
        return -10
    elif a[2]==b[2] and b[1]<a[1]:
        return 10
r,w=input().split()
w=int(w)
r=int(r)
matrix=[0]*(r+1)
for i in range(r+1):
    matrix[i]=[0]*(w+1)
structarray=[0]*(r*w)
a=0
for i in range(1,r+1):
    for j in range(1,w+1):
        disy=i-1
        disx=j-((w+1)//2)
        dis=(disy**2)+(disx**2)
        structarray[a]=i,j,dis
        a+=1
from functools import cmp_to_key
structarray = sorted(structarray, key=cmp_to_key(comp))
for i in range(r*w):
    matrix[structarray[i][0]][structarray[i][1]]=i+1
for i in range(r,0,-1):
    for j in range(1,w+1):
        print(matrix[i][j],end=" ")
    print()
'''