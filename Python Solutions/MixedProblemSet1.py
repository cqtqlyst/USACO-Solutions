'''
num=int(input())
ordarr=[int(i) for i in input().split()]
idarr=[int(i) for i in input().split()]
nextidarr=[0]*num
for j in range(3):
    for i in range(num):
        nextidarr[ordarr[i]-1]=idarr[i]
        for a in range(num):
            idarr[a]=nextidarr[a]
for i in range(num):
    print(idarr[i])

row,col=input().split()
row=int(row)
col=int(col)
maxi=0
matrix=[0]*row
save1=0
save2=0
for i in range(row):
    matrix[i]=[0]*col
for i in range(row):
    matrix[i]=[int(j) for j in input().split()]
for r in range(row-2):
    for c in range(col-2):
        actual=matrix[r][c]+matrix[r][c+1]+matrix[r][c+2]+matrix[r+1][c]+matrix[r+1][c+1]+matrix[r+1][c+2]+matrix[r+2][c]+matrix[r+2][c+1]+matrix[r+2][c+2]
        if actual>maxi:
            maxi=actual
            save1=r+1
            save2=c+1
print(maxi)
print(save1,save2)

num,k=input().split()
num=int(num)
k=int(k)
row=0
matrix=[" "]*num
for i in range(num):
    matrix[i]=[" "]*num
for c in range(num):
    for r in range(row+1):
        matrix[r][c]=k
        if k==9:
            k=0
        k=(k%10)+1
    row+=1
for i in range(num):
    for j in range(num):
        print(str(matrix[i][j]),end=" ")
    print("")
'''
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string=input()
start=[0]*26
finish=[0]*26
counter=[0]*26
check=0
for i in range(26):
    c=alph[i]
    check=0
    for j in range(52):
        if string[j]=c:
            if check=0:
                start[i]+=1
            else:
                end[i]+=1
for i in range(26):
    for j in range(start[i]+1,end[i]):
        c=string[j]
        num=alph.find(c)
        counter[num]+=1
    for x in range(26):
        















