'''
line = input().split()
pos = 0
def readInt():
    global pos, line
    if pos >= len(line):
        line = input().split()
        pos = 0
    pos += 1
    return int(line[pos - 1])
a=readInt()
b=readInt()
e=a+1
multiply=0
while multiply!=b:
    multiply=2**e
    while multiply>9:
        multiply=multiply//10
    if multiply==b:
        print(multiply)
    e=e+1
'''
line = input().split()
pos = 0
def readInt():
    global pos, line
    if pos >= len(line):
        line = input().split()
        pos = 0
    pos += 1
    return int(line[pos - 1])
numofcows=readInt()
array=[-1]*11
numofc=0
for i in range(numofcows):
    i=readInt()
    x=readInt()
    if array[i]!=-1:
        if array[i]!=x:
            numofc=numofc+1
    array[i]=x
print(numofc)
        
    
    
    
    
    
    
    
    
    
    
    
    