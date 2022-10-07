'''
numofcows=int(input())
arrayx=[0]*numofcows
arrayy=[0]*numofcows
arrayr=[0]*numofcows
overlap=0
for i in range(numofcows):
    arrayx[i],arrayy[i],arrayr[i]=input().split()
    arrayx[i]=int(arrayx[i])
    arrayy[i]=int(arrayy[i])
    arrayr[i]=int(arrayr[i])
for i in range(numofcows):
    for x in range(numofcows):
        actual=((arrayx[i]-arrayx[x])**2)+((arrayy[i]-arrayy[x])**2)
        if i!=x:
            if ((arrayr[i]+arrayr[x])**2)>actual:
                overlap=overlap+1
    print(overlap)
    overlap=0
'''
dice1,dice2,dice3=input().split()
dice1=int(dice1)
dice2=int(dice2)
dice3=int(dice3)
maxi=0
freq=[0]*8001
actual=0
for i in range(1,dice1+1):
    for x in range(1,dice2+1):
        for a in range(1,dice3+1):
            summy=i+x+a
            freq[summy]=freq[summy]+1
for i in range(1,8001):
    if freq[i]>maxi:
        maxi=freq[i]
        actual=i
print(actual)