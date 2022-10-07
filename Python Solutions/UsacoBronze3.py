'''
x,y,m=input().split()
x=int(x)
y=int(y)
m=int(m)
total=0
count=0
maximum=0
count2=0
Maxx=m//x
Maxx=int(Maxx)
Maxy=m//y
Maxy=int(Maxy)
for count in range(0,Maxx+1):
    for count2 in range(0,Maxy+1):
        total=(count*x)+(count2*y)
        if total<=m:
            if total>maximum:
                maximum=total
print(maximum)

score=0
n=int(input())
while n!=1:
    while n%2==1:
        n=(n*3)+1
        score=score+1
    while n%2==0:
        n=n//2
        score=score+1
print(score)
'''


