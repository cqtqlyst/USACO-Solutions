#Dream Counting

start,end=input().split()
start=int(start)
end=int(end)
counter0=0
counter1=0
counter2=0
counter3=0
counter4=0
counter5=0
counter6=0
counter7=0
counter8=0
counter9=0
for i in range(start,end+1):
    if i%10==0:
        counter0=counter0+1
    if i%10==1:
        counter1=counter1+1
    if i%10==2:
        counter2=counter2+1
    if i%10==3:
        counter3=counter3+1
    if i%10==4:
        counter4=counter4+1
    if i%10==5:
        counter5=counter5+1
    if i%10==6:
        counter6=counter6+1
    if i%10==7:
        counter7=counter7+1
    if i%10==8:
        counter8=counter8+1
    if i%10==9:
        counter9=counter9+1
print(counter0,counter1,counter2,counter3,counter4,counter5,counter6,counter7,counter8,counter9)
'''
#Barn Echoes
string1=input()
string2=input()
maxi=0
n=0
for i in range(len(string1)):
    for j in range(i,len(string1)):
        size=abs(i-j)
        for a in range(len(string2)):
            for b in range(a,len(string2)):
                if abs(a-b)!=size:
                    n=1
                elif string1[i:j]==string2[a:b]:
                    if size>maxi:
                        maxi=size
                        print(maxi)
print(maxi+1)

#Going once, Going twice, Gone!
numoflots,numoffarmers=input().split()
numoflots=int(numoflots)
numoffarmers=int(numoffarmers)
array=[0]*numoffarmers
maximum=0
maxi=0
counter=0
price=0
check=0
for i in range(numoffarmers):
    array[i]=int(input())
for i in range(numoffarmers):
    if array[i]>maximum:
        maximum=array[i]
for i in range(numoffarmers):
    check=array[i]
    for j in range(numoffarmers):
        if array[j]>=check:
            counter=counter+1
    if counter>numoflots:
        counter=0
    elif (counter*check)>maxi:
        maxi=counter*check
        price=check
    counter=0
print(price,maxi)
'''











