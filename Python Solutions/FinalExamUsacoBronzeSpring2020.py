'''
num=int(input())
array=[0]*num
for i in range(num):
    start,end=input().split()
    start=int(start)
    end=int(end)
    array[i]=start,end
marked=[0]*1001
maxi=0
for i in range(num):
    numofmark=0
    marked=[0]*1001
    for j in range(num):
        if j!=i:
            for a in range((array[j][0]+1),array[j][1]+1):
                marked[a]=1
    for i in range(1001):
        if marked[i]==1:
            numofmark+=1
    if numofmark>maxi:
        maxi=numofmark
print(maxi)

num=int(input())
array=[0]*num
array=[int(i) for i in input().split()]
sortarray=[0]*num
for i in range(num):
    sortarray[i]=array[i]
sortarray.sort()
ctr=0
while True:
    ctr+=1
    control=array[0]
    newarray=[0]*num
    for i in range(num):
        if array[i]==control-1 or (control==1 and array[i]==num):
            for j in range(i):
                newarray[j]=array[j+1]
            newarray[i]=control
            for j in range(i+1,num):
                newarray[j]=array[j]
            break
    for i in range(num):
        array[i]=newarray[i]
    check=True
    for i in range(num):
        if array[i]!=sortarray[i]:
            check=False
    if check==True:
        break
print(ctr)
'''
row,col=input().split()
row=int(row)
col=int(col)
matrix=[0]*row
for i in range(row):
    matrix[i]=[0]*col
array=[0]*col
for i in range(row):
    string=input()
    for j in range(col):
        matrix[i][j]=string[j]
startrow,startcol=input().split()
startrow=int(startrow)
startcol=int(startcol)
ctr=0
print(matrix)
infinite=False
maxi=0
direction=""
currentrow=startrow
currentcol=startcol
currentdirection="U"
while True:
    ctr+=1
    if currentdirection=="U":
        currentrow-=1
        if currentrow<0:
            break
        if matrix[currentrow][currentcol]=="C":
            break
        if matrix[currentrow][currentcol]=="/":
            currentdirection="R"
        if matrix[currentrow][currentcol]=="\\":
            currentdirection="L"
    elif currentdirection=="R":
        currentcol+=1
        if currentcol>col-1:
            break
        if matrix[currentrow][currentcol]=="C":
            break
        if matrix[currentrow][currentcol]=="/":
            currentdirection="U"
        if matrix[currentrow][currentcol]=="\\":
            currentdirection="D"
    elif currentdirection=="D":
        currentrow+=1
        if currentrow>row-1:
            break
        if matrix[currentrow][currentcol]=="C":
            break
        if matrix[currentrow][currentcol]=="/":
            currentdirection="L"
        if matrix[currentrow][currentcol]=="\\":
            currentdirection="R"
    elif currentdirection=="L":
        currentcol-=1
        if currentcol<0:
            break
        if matrix[currentrow][currentcol]=="C":
            break
        if matrix[currentrow][currentcol]=="/":
            currentdirection="D"
        if matrix[currentrow][currentcol]=="\\":
            currentdirection="U"
    if currentrow==startrow and currentcol==startcol:
        infinite=True
        direction="U"
        print(direction)
        print("Voyager")
        break
if infinite==False and ctr>maxi:
    maxi=ctr
ctr=0
currentrow=startrow
currentcol=startcol
currentdirection="R"
if infinite==False:
    while True:
        ctr+=1
        if currentdirection=="U":
            currentrow-=1
            if currentrow<0:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="R"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="L"
        elif currentdirection=="R":
            currentcol+=1
            if currentcol>col-1:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="U"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="D"
        elif currentdirection=="D":
            currentrow+=1
            if currentrow>row-1:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="L"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="R"
        elif currentdirection=="L":
            currentcol-=1
            if currentcol<0:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="D"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="U"
        if currentrow==startrow and currentcol==startcol:
            infinite=True
            direction="R"
            print(direction)
            print("Voyager")
            break
    if infinite==False and ctr>maxi:
        maxi=ctr
ctr=0
currentrow=startrow
currentcol=startcol
currentdirection="D"
if infinite==False:
    while True:
        ctr+=1
        if currentdirection=="U":
            currentrow-=1
            if currentrow<0:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="R"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="L"
        elif currentdirection=="R":
            currentcol+=1
            if currentcol>col-1:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="U"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="D"
        elif currentdirection=="D":
            currentrow+=1
            if currentrow>row-1:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="L"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="R"
        elif currentdirection=="L":
            currentcol-=1
            if currentcol<0:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="D"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="U"
        if currentrow==startrow and currentcol==startcol:
            infinite=True
            direction="D"
            print(direction)
            print("Voyager")
            break
    if infinite==False and ctr>maxi:
        maxi=ctr
ctr=0
currentrow=startrow
currentcol=startcol
currentdirection="L"
if infinite==False:
    while True:
        ctr+=1
        if currentdirection=="U":
            currentrow-=1
            if currentrow<0:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="R"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="L"
        elif currentdirection=="R":
            currentcol+=1
            if currentcol>col-1:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="U"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="D"
        elif currentdirection=="D":
            currentrow+=1
            if currentrow>row-1:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="L"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="R"
        elif currentdirection=="L":
            currentcol-=1
            if currentcol<0:
                break
            if matrix[currentrow][currentcol]=="C":
                break
            if matrix[currentrow][currentcol]=="/":
                currentdirection="D"
            if matrix[currentrow][currentcol]=="\\":
                currentdirection="U"
        if currentrow==startrow and currentcol==startcol:
            infinite=True
            direction="L"
            print(direction)
            print("Voyager")
            break
    if infinite==False and ctr>maxi:
        maxi=ctr