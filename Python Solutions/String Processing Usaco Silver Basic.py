'''
def bs(array,num,find):
    mini=0
    maxi=num-1
    a=0
    while mini<=maxi:
        midi=(mini+maxi)//2
        a=0
        for i in range(min(len(find),len(array[midi]))):
            if array[midi][i]==find[i]:
                a=0
            else:
                a=1
                break
        if a==0:
            return midi
        if find>array[midi]:
            mini=midi+1
        elif find<array[midi]:
            maxi=midi-1
    return -1
m,n=input().split()
m=int(m)
n=int(n)
ctr=0
phrasebook=[0]*m
for i in range(m):
    phrasebook[i]=input()
phrasebook.sort()
for i in range(n):
    string=input()
    if bs(phrasebook,m,string)!=-1:
        ctr+=1
print(ctr)
'''
n=int(input())
array=[0]*n
for i in range(n):
    num,correct,wrongloc=input().split()
    num=int(num)
    correct=int(correct)
    wrongloc=int(wrongloc)
    array[i]=num,correct,wrongloc