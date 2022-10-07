'''
bx1,by1,bx2,by2=input().split()
bx1=int(bx1)
by1=int(by1)
bx2=int(bx2)
by2=int(by2)
gx1,gy1,gx2,gy2=input().split()
gx1=int(gx1)
gy1=int(gy1)
gx2=int(gx2)
gy2=int(gy2)
covered=0
if (gy2<by2 and gy1>by1) or (gx2<bx2 and gx1>bx1):
    covered=0
elif (gx1<=bx1 and gx2>=bx2):
    if (min(gy2,by2))>(max(gy1,by1)):
        covered=(min(gy2,by2)-max(gy1,by1))*(bx2-bx1)
elif (gy1<=gy2 and gy2>=by2):
    if (min(gx2,bx2))>(max(gx1,bx1)):
        covered=(min(gx2,bx2)-max(gx1,gx1))*(bx2-bx1)
area=(bx2-bx1)*(by2-by1)
print(area-covered)

b1x1,b1y1,b1x2,b1y2=input().split()
b1y1=int(b1y1)+1000
b1x1=int(b1x1)+1000
b1x2=int(b1x2)+1000
b1y2=int(b1y2)+1000
b2x1,b2y1,b2x2,b2y2=input().split()
b2y1=int(b2y1)+1000
b2x1=int(b2x1)+1000
b2x2=int(b2x2)+1000
b2y2=int(b2y2)+1000
t1x1,t1y1,t1x2,t1y2=input().split()
t1y1=int(t1y1)+1000
t1x1=int(t1x1)+1000
t1x2=int(t1x2)+1000
t1y2=int(t1y2)+1000
counter=0
for x in range(b1x1,b1x2):
    for y in range(b1y1,b1y2):
        if x>=t1x1 and x<t1x2 and y>=t1y1 and y<t1y2:
            j=0
        else:
            counter=counter+1
for x in range(b2x1,b2x2):
    for y in range(b2y1,b2y2):
        if x>=t1x1 and x<t1x2 and y>=t1y1 and y<t1y2:
            j=0
        else:
            counter=counter+1
print(counter)
'''
num,b=input().split()
num=int(num)
b=int(b)
points=[0]*n
for i in range(n):
    points[i]=[0]*2
for j in range(n):
    points[j]=[int(i) for i in input().split()]
maxcow=0
minmax=10000000000000000000000000000000000000000000000
for ix in range(num):
    a=(points[ix][0])+1
    for iy in range(num):
        b=(points[iy][1])+1
        c1=0
        c2=0
        c3=0
        c4=0
        for i in range(n):
            if points[i][0]<a and points[i][1]<b:
                c1+=1
            elif points[i][0]<a and points[i][1]>b:
                c2+=1
            elif points[i][0]>a and points[i][1]<b:
                c3+=1
            else:
                c4+=1
        maxcow=max(max(c1,c2),max(c3,c4))
        minmax=min(maxcow,minmax)
print(minmax)