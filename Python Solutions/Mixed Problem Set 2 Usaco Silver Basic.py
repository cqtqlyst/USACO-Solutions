'''
n=int(input())
counter=0
for i in range(1,(2**n)):
    number=i
    result=""
    while number>0:
        result=(str(number%2))+result
        number=number//2
    numof0=0
    numof1=0
    s=""
    for j in range(n-len(result)):
        s+="0"
    result=s+result
    for j in range(n):
        if result[j]=="1":
            numof1+=1
        else:
            numof0+=1
    if numof1>numof0:
        print(result)
        counter+=1
print(counter)

def skewsort(l,r):
    global array
    mid=(l+r)//2
    if l==r:
        return
    skewsort(l,mid)
    skewsort(mid+1,r)
    if array[l]>array[mid+1]:
        swap(l,mid,mid+1,r)
    return 
def swap(l,mid,mid2,r):
    global array
    global numofmove
    numofmove+=(mid2-l)*((mid-l+1)+(r-mid2+1))
    newarr=[0]*(mid-l+1)
    index=l
    for i in range(mid-l+1):
        newarr[i]=array[index]
        index+=1
    index=l
    for i in range(mid2,r+1):
        array[index]=array[i]
        index+=1
    index=0
    for i in range(mid2,r+1):
        array[i]=newarr[index]
        index+=1      
n=int(input())
array=[0]*(2**n)
for i in range(2**n):
    array[i]=int(input())
numofmove=0
skewsort(0,2**n-1)
print(numofmove)
for i in range(2**n):
    print(array[i])
'''
