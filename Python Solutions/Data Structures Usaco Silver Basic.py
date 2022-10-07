'''
n=int(input())
stack=[]
j=1
for i in range(n):
    string=input()
    if string=="ADD":
        stack.append(j)
        j+=1
    else:
        stack.pop()
print(len(stack))
for i in range(len(stack)):
    print(stack[i])

dirty=[]
wet=[]
yay=[]
n=int(input())
for i in range(n,0,-1):
    dirty.append(i)
while len(yay)!=n:
    c,d=input().split()
    c=int(c)
    d=int(d)
    for i in range(d):
        if c==1:
            wet.append(dirty[-1])
            dirty.pop()
        else:
            yay.append(wet[-1])
            wet.pop()
for i in range(n):
    print(yay[n-i-1])
'''
import sys
import queue
q=queue.Queue()
n=int(input())
array=[[] for i in range(n)]
while True:
    try:
        char,num=input().split()
        num=int(num)
    except EOFError:
        break
    if char=="C":
        q.put(num)
    else:
        save=q.get()
        (array[num-1]).append(save)
for i in range(n):
    print(len(array[i]),end=" ")
    for j in range(len(array[i])):
        print(array[i][j],end=" ")
    print()
