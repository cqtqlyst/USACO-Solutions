'''
import math
n=int(input())
pairs=0
for b in range(1,501):
    a=math.sqrt(b**2+n)
    if a%1==0:
        pairs=pairs+1
print(pairs)

line = input().split()
pos = 0
def readInt():
    global pos, line
    if pos >= len(line):
        line = input().split()
        pos = 0
    pos += 1
    return int(line[pos - 1])
numofpulleys=readInt()
cc=0
c=0
for i in range(1,numofpulleys):
    x=readInt()
    y=readInt()
    ccorc=readInt()
    if ccorc==1:
        cc=cc+1
    else:
        c=c+1
if cc%2==1:
    print(1)
else:
    print(0)
    '''