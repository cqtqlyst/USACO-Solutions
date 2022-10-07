'''
import sys
def ff(row,col):
    global visited
    global cursize
    global dy
    global dx
    global h
    global w
    visited[row][col]=1
    cursize+=1
    for i in range(8):
        newrow=row+dy[i]
        newcol=col+dx[i]
        if newrow<h and newrow>=0 and newcol<w and newcol>=0:
            if visited[newrow][newcol]==0:
                if array[newrow][newcol]==".":
                    ff(newrow,newcol)
sys.setrecursionlimit(750*750)
w,h=input().split()
w=int(w)
h=int(h)
dx=[1,1,1,0,0,-1,-1,-1]
dy=[1,0,-1,1,-1,1,0,-1]
array=[0]*(h+1)
visited=[0]*(h+1)
for i in range(h):
    array[i]=[0]*(w+1)
    visited[i]=[0]*(w+1)
for i in range(h):
    string=input()
    for j in range(w):
        array[i][j]=string[j]
ans=0
x=0
for i in range(h):
    for j in range(w):
        if visited[i][j]==0 and array[i][j]!="*":
            cursize=0
            ff(i,j)
            ans=max(ans,cursize)
            if ans>(h*w)/2:
                x=1
                break
    if x==1:
        break
print(ans)
'''
def
n=int(input())
array=[0]*n
for i in range(n):
    array[i]=[0]*n
for i in range(n):
    array[i]=[j for j in input().split()]
visited=[0]*n
for i in range(n):
    visited[i]=[0]*n
dfs(0,0,1,0)