'''
def compsec(a):
    return a[2]
def compmin(b):
    return b[1]
def comphour(c):
    return c[0]
n=int(input())
array=[0]*n
for i in range(n):
    hour,minute,sec=input().split()
    hour=int(hour)
    minute=int(minute)
    sec=int(sec)
    array[i]=hour,minute,sec
array.sort(key=compsec)
array.sort(key=compmin)
array.sort(key=comphour)
for i in range(n):
    print(str(array[i][0]) + " " + str(array[i][1]) + " " + str(array[i][2]))

def comp(a):
    return[0]
n=int(input())
array=[0]*n
for i in range(n):
    day,cow,plusminus=input().split()
    day=int(day)
    plusminus=int(plusminus)
    array[i]=day,cow,plusminus
counter=0
toplist=""
prevstring="bem"
array.sort(key=comp)
b=0
m=0
e=0
actual=0
for i in range(n):
    if array[i][1]=="Bessie":
        b=b+array[i][2]
    elif array[i][1]=="Elsie":
        e=e+array[i][2]
    else:
        m=m+array[i][2]
    if b>=e and b>=m:
        toplist=toplist+"b"
    if e>=b and e>=m:
        toplist=toplist+"e"
    if m>=b and m>=e:
        toplist=toplist+"m"
    if toplist!=prevstring:
        counter=counter+1
    prevstring=toplist
    toplist=""
print(counter)
'''
def comp(c):
    return -c[2]
num=int(input())
array=[0]*num
for i in range(num):
    joy,price=input().split()
    joy=int(joy)
    price=int(price)
    hfm=joy/price
    toynumber=i+1
    array[i]=toynumber,price,hfm
array.sort(key=comp)
print(array[0][1] + array[1][1] + array[2][1])
for i in range(3):
    print(array[i][0])









