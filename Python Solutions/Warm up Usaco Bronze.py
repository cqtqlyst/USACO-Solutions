'''
numofcows=int(input())
xarray=[0]*numofcows
yarray=[0]*numofcows
maxdis=0
cow1=0
cow2=0
for i in range(numofcows):
    x,y=input().split()
    x=int(x)
    y=int(y)
    xarray[i]=x
    yarray[i]=y
for i in range(numofcows-1):
    n=i+1
    while n<numofcows:
        distance=((xarray[n]-xarray[i])**2)+((yarray[n]-yarray[i])**2)
        if distance>maxdis:
            maxdis=distance
            cow1=i+1
            cow2=n+1
        n=n+1
    n=0
print(str(cow1)+" "+str(cow2))

bracesize,numofcharms,nail=input().split()
bracesize=int(bracesize)
numofcharms=int(numofcharms)
nail=int(nail)
for i in range(numofcharms):
    size,location=input().split()
    size=int(size)
    location=int(location)
    distance=abs((nail-location))+size
    print(distance)

length,width=input().split()
length=int(length)
width=int(width)
numofcows=0
while length%2==1 and width%2==1:
    width=width//2
    length=length//2
    numofcows=(numofcows*4)+1
print(numofcows)
'''     
numofrows,numofcol,numofdupli=input().split()
numofrows=int(numofrows)
numofcol=int(numofcol)
numofdupli=int(numofdupli)
string=[" "]*numofrows
string2=[" "]*(numofrows*numofdupli)
for i in range(numofrows):
    s=input()
    s2 = ""
    for j in range(numofcol):
        for t in range(numofdupli):
            s2 = s2 + s[j]
    for u in range(numofdupli):
        print(s2)
    
    
    
    
    
    
    