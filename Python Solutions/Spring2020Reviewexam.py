'''
up,down,total=input().split()
up=int(up)
down=int(down)
total=int(total)
diff=up-down
answer=(total-up)//(up-down)
if (answer*(up-down))+up>=total:
    print(answer+1)
else:
    print(answer+2)

n=int(input())
array=[0]*n
medarray=[0]*n
for i in range(n):
    array=[int(i) for i in input().split()]
    array.sort()
    medi=n/2
    medi=int(medi)
    medarray[i]=array[medi]
medarray.sort()
medi=n/2
medi=int(medi)
print(medarray[medi])
'''
def comp(s):
    return s[0]
n=int(input())
array=[0]*n
for i in range(n):
    start,end,buckets=input().split()
    start=int(start)
    end=int(end)
    buckets=int(buckets)
    array[i]=start,end,buckets
array.sort(key=comp)
timeline=[0]*100000000
maxi=0
for i in range(n):
    for j in range(array[i][0],array[i][1]):
        timeline[j]+=1
for i in range(100000000):
    if timeline[i]>maxi:
        maxi=timeline[i]
print(maxi)