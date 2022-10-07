'''
num=int(input())
num-=1
total=0
for i in range(num):
    x,y,turn=input().split()
    turn=int(turn)
    total+=turn
print(total%2)

num=int(input())
array=[0]*num
index=0
ctr=0
for i in range(num):
    day=int(input())
    if day!=1:
        dif=day-1
        found=False
        for j in range(index):
            if dif%array[j]==0:
                found=True
        if found==False:
            array[index]=dif
            index+=1
            ctr+=1
print(ctr)
'''
s1,s2=input().split()
mins1=""
maxs1=""
for i in range(len(s1)):
    if s1[i]=="6":
        mins1+="5"
    else:
        mins1+=s1[i]
    if s1[i]=="5":
        maxs1+="6"
    else:
        maxs1+=s1[i]
mins2=""
maxs2=""
for i in range(len(s2)):
    if s2[i]=="6":
        mins2+="5"
    else:
        mins2+=s2[i]
    if s2[i]=="5":
        maxs2+="6"
    else:
        maxs2+=s2[i]
mini=int(mins1)+int(mins2)
maxi=int(maxs1)+int(maxs2)
print(mini,maxi)