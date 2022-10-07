'''
num=int(input())
a=0
b=0
c=0
d=0
counter=0
while (a*a)<num:
    while ((a*a)+(b*b))<=num:
        b=0
        c=0
        d=0
        while ((a*a)+(b*b)+(c*c))<=num:
            while ((a*a)+(b*b)+(c*c)+(d*d))<=num:
                if ((a*a)+(b*b)+(c*c)+(d*d))==num:
                    counter=counter+1
                d=d+1
            c=c+1
        b=b+1
    a=a+1
print(counter)

numofrooms=int(input())
array=[0]*numofrooms
for i in range(numofrooms):
    array[i]=int(input())
n=1
mindistance=0
for sindex in range(numofrooms):
    counter=0
    index=sindex
    distance=0
    while counter<numofrooms:
        distance=distance+(array[index]*counter)
        index=(index+1)%numofrooms
        counter=counter+1
    if n==1:
        mindistance=distance
        n=2
    if distance<mindistance:
        mindistance=distance
print(mindistance)
'''
numofgames=int(input())
counter1=0
counter2=0
for i in range(numofgames):
    n1,n2=input().split()
    n1=int(n1)
    n2=int(n2)
    if (n1==1 and n2==2) or (n1==2 and n2==3) or (n1==3 and n2==1):
        counter1=counter1+1
    elif (n1==1 and n2==3) or (n1==3 and n2==2) or (n1==2 and n2==1):
        counter2=counter2+1
print(max(counter1,counter2))
        
        
        