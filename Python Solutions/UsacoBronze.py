'''
x1,y1,x2,y2=input().split()
x3,y3,x4,y4=input().split()
x1=int(x1)
x2=int(x2)
x3=int(x3)
x4=int(x4)
y1=int(y1)
y2=int(y2)
y3=int(y3)
y4=int(y4)
if x1>=x2 and x1>=x3 and x1>=x4:
    greatestx=x1
elif x2>=x1 and x2>=x3 and x2>=x4:
    greatestx=x2
elif x3>=x1 and x3>=x2 and x3>=x4:
    greatestx=x3
else:
    greatestx=x4
if x1<=x2 and x1<=x3 and x1<=x4:
    leastx=x1
elif x2<=x1 and x2<=x3 and x2<=x4:
    leastx=x2
elif x3<=x1 and x3<=x2 and x3<=x4:
    leastx=x3
else:
    leastx=x4
if y1>=y2 and y1>=y3 and y1>=y4:
    greatesty=y1
elif y2>=y1 and y2>=y3 and y2>=y4:
    greatesty=y2
elif y3>=y1 and y3>=y2 and y3>=y4:
    greatesty=y3
else:
    greatesty=y4
if y1<=y2 and y1<=y3 and y1<=y4:
    leasty=y1
elif y2<=y1 and y2<=y3 and y2<=y4:
    leasty=y2
elif y3<=y1 and y3<=y2 and y3<=y4:
    leasty=y3
else:
    leasty=y4
ly=greatesty-leasty
lx=greatestx-leastx
if ly>lx:
    area=ly*ly
else:
    area=lx*lx
print(area)
'''
d,h,m=input().split()
d=int(d)
h=int(h)
m=int(m)
nday=(d-11)*1440
nhour=(h-11)*60
nmin=m-11
print(nmin)
f=nday+nhour+nmin
if f<0:
    print("-1")
else:
    print(f)