'''
numofnum=int(input())
for i in range(numofnum):
    n=int(input())
    if n%2==1:
        print("odd")
    else:
        print("even")

num=input()
size=len(num)
for i in range(size):
    print(num[i],end="")
    if (i+1)%3==size%3 and i!=size-1:
        print(",",end="")
'''
numofwords=int(input())
for i in range(numofwords):
    addindex,times,word=input().split()
    addindex=int(addindex)
    times=int(times)
    for x in range(times):
        word=word[addindex:]+word
    print(word)