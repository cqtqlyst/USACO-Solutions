'''
num,base=input().split()
base=int(base)
multi=1
total=0
for i in range((len(num)-1),-1,-1):
    word=int(num[i])
    total+=multi*word
    multi*=base
print(total)

num,base=input().split()
base=int(base)
number=int(num)
result=""
while number>0:
    result=(str(number%base))+result
    number=number//base
print(result)

num=input()
base=2
multi=1
total=0
for i in range((len(num)-1),-1,-1):
    word=int(num[i])
    total+=multi*word
    multi*=base
number=total*17
result=""
while number>0:
    result=(str(number%base))+result
    number=number//base
print(result)
'''
nums=input()
length=len(nums)
numb=""
for i in range(length):
    c=nums[i]
    if c>="A" and c<="F":
        value=(int(ord(c))-int(ord("A")))+10
    else:
        value=int(c)
    value=int(value)
    result=""
    while value>0:
        result=(str(value%2))+result
        value=value//2
    while len(result)<4:
        result="0"+result
    numb=numb+result
if len(numb)%3!=0:
    while len(numb)%3!=0:
        numb="0"+numb
actualtotal=""
for i in range(0,(len(numb)),3):
    num=numb[i:i+3]
    base=2
    multi=1
    total=0
    for i in range((len(num)-1),-1,-1):
        word=int(num[i])
        total+=multi*word
        multi*=base
    actualtotal=actualtotal+str(total)
if actualtotal[0]=="0":
    actualtotal=actualtotal[1:len(actualtotal)]
print(actualtotal)