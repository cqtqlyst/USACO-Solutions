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
maximum=readInt()
count=0
current=readInt()
for i in range(1,maximum):
    last=current
    current=readInt()
    if last!=current:
        count=count+1
print(count)

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
x=readInt()
y=readInt()
total1=abs(a-b)
total2=abs(a-y)+abs(b-x)
total3=abs(b-y)+abs(a-x)
actual=min(total1,total2,total3)
print(actual)
'''




