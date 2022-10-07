'''
def dfs(a,b,sume):
    global ans
    global r
    global matrix
    sume+=matrix[a][b]
    if a==r:
        if sume>ans:
            ans=sume
        return
    dfs(a+1,b,sume)
    dfs(a+1,b+1,sume)
r=int(input())
matrix=[0]*(r+1)
for i in range(r+1):
    matrix[i]=[0]*(r+1)
for i in range(1,r+1):
    arr=[0]*i
    arr=[int(j) for j in input().split()]
    for j in range(i):
        matrix[i][j+1]=arr[j]
ans=0
dfs(1,1,0)
print(ans)
'''
