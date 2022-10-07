'''
num=int(input())
n=1
stringnum=str(num)
counter=0
array=[0]*len(stringnum)
for i in range(len(stringnum)):
    array[i]=stringnum[i]
string=""
print(array)
while n==1:
    for i in range(len(stringnum)//2):
        save=stringnum[i]
        array[i]=stringnum[len(stringnum)-i-1]
        array[len(stringnum)-i-1]=save
    for i in range(len(stringnum)):
        string+=array[i]
    total=int(string)+num
    num=total
    stringnum=str(num)
    array=[0]*len(stringnum)
    for i in range(len(stringnum)):
        array[i]=stringnum[i]
    counter+=1
    total=str(total)
    check=0
    for i in range(len(total)//2):
        if total[i]!=total[len(stringnum)-i-1]:
            check=1
    if check==0:
        n=0
    check=0
print(str(counter-1) + str(num))

num=int(input())
array=[0]*num
array2=[0]*num
for i in range(num):
    array[i]=int(input())
    array2[i]=array[i]
array2.sort()
blocation=0
maxi=0
save=0
n=1
x=1
counter=0
array3=[0]*num
for i in range(num):
    for j in range(num):
        if array[i]==array2[j]:
            array3[i]=abs(i-j)
for i in range(num):
    if array3[i]>maxi:
        maxi=array3[i]
        save=i
for i in range(num):
    if array2[i]==array[save]:
        save2=i
if save>save2:
    current=save
    furthest=save-1
    while n=1:
        while x=1:
            if array[furthest]==array[furthest-1]:
                furthest=furthest-1
            else:
                break
        array[furthest]=array[save]
        save=furthest
        furthest=save-1
        counter+=1
        if array[save]=array2[save]:
            break
    print(counter)
'''
def comp(c):
    return c[0]
numofcows,advance=input().split()
numofcows=int(numofcows)
advance=int(advance)
array=[0]*numofcows
for i in range(numofcows):
    r1,r2=input().split()
    r1=int(r1)
    r2=int(r2)
    array[i]=r1,r2,i
array.sort(key=comp)
print(array)
array2=[0]*advance
array3=[0]*advance
for i in range(advance):
    array2[i]=array[numofcows-i-1][1],array[numofcows-i-1][2]
print(array2)
array2.sort()
print(array2[advance-1][0])






    
        
        
    


