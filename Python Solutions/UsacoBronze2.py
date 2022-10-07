'''
n=int(input())
sum=0
count=1
while count<=n:
    if n%count==0:
        sum=sum+count
    count=count+1
print(sum)

bb,ba=input().split()
sb,sa=input().split()
gb,ga=input().split()
pb,pa=input().split()
bb=int(bb)
ba=int(ba)
sb=int(sb)
sa=int(sa)
gb=int(gb)
ga=int(ga)
pb=int(pb)
pa=int(pa)
totalbf=bb+sb+gb+pb
totalaf=ba+sa+ga+pa
newstud=totalaf-totalbf
btot=newstud+bb
bspro=btot-ba
print(bspro)
stot=bspro+sb
sgpro=stot-sa
print(sgpro)
gtot=sgpro+gb
gppro=gtot-ga
print(gppro)
'''