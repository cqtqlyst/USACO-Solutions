'''
fin=open("gymnastics.in", "r")
fout=open("gymnastics.out", "w")
numoflines,numofcows=map(int,fin.readline().split())
numoflines=int(numoflines)
numofcows=int(numofcows)
array=[0]*numoflines
for i in range(numoflines):
    array[i]=[0]*numofcows
for i in range(numoflines):
    for j in range(numofcows):
        array[i]=fin.readline().split()
true=0
for first in range(numofcows):
    for second in range(numofcows):
        if first!=second:
            for line in range(numoflines):
                for index1 in range(numofcows):
                    if array[line][index1]==first:
                        firsti=index1
                for index2 in range(numofcows):
                    if array[line][index2]==second:
                        secondi=index2
                if firsti>secondi:
                    true=1
            if true==0:
                counter=counter+1
        true=0
fout.write(str(counter)+'/n')
fout.close()

fin=open("whereami.in", "r")
fout=open("whereami.out", "w")
num=int(fin.readline())
string=fin.readline()
counter=1
for i in range(num):
    for j in range(i+1,num):
        if abs(j-i)==counter:
            for x in range(i+1,num):
                for y in range(j+1,num):
                    if abs(y-x)==counter:
                        if string[i:j+1]==string[x:y+1]:
                            counter=counter+1
fout.write(str(counter+1))
fout.close()
'''
fin=open("lineup.in", "r")
fout=open("lineup.out", "w")
numofclues=int(fin.readline())
arrayofclues=[0]*numofclues
for i in range(numofclues):
    a,b,c,d,e,f=fin.readline().split()
    arrayofclues[i]=a,f
array=[0]*8
array[0]="Beatrice"
array[1]="Belinda"
array[2]="Bella"
array[3]="Bessie"
array[4]="Betsy"
array[5]="Blue"
array[6]="Buttercup"
array[7]="Sue"
array2=[0]*8
leave=0
for a in range(8):
    if leave==1:
        break
    for b in range(8):
        if leave==1:
            break
        if b!=a:
            for c in range(8):
                if leave==1:
                    break
                if c!=a and c!=b:
                    for d in range(8):
                        if leave==1:
                            break
                        if d!=a and d!=b and d!=c:
                            for e in range(8):
                                if leave==1:
                                    break
                                if e!=a and e!=b and e!=c and e!=d:
                                    for f in range(8):
                                        if leave==1:
                                            break
                                        if f!=a and f!=b and f!=c and f!=d and f!=e:
                                            for g in range(8):
                                                if leave==1:
                                                    break
                                                if g!=a and g!=b and g!=c and g!=d and g!=e and g!=f:
                                                    for h in range(8):
                                                        if leave==1:
                                                            break
                                                        if h!=a and h!=b and h!=c and h!=d and h!=e and h!=f and h!=g:
                                                            array2[0]=array[a]
                                                            array2[1]=array[b]
                                                            array2[2]=array[c]
                                                            array2[3]=array[d]
                                                            array2[4]=array[e]
                                                            array2[5]=array[f]
                                                            array2[6]=array[g]
                                                            array2[7]=array[h]
                                                            for i in range(numofclues):
                                                                for j in range(8):
                                                                    if array2[j]==arrayofclues[i][0]:
                                                                        alocation=j
                                                                    elif array2[j]==arrayofclues[i][1]:
                                                                        blocation=j
                                                                if alocation+1==blocation or alocation-1==blocation:
                                                                    true=0
                                                                else:
                                                                    true=1
                                                            if true==0:
                                                                fout.write(array2[0]+"\n")
                                                                fout.write(array2[1]+"\n")
                                                                fout.write(array2[2]+"\n")
                                                                fout.write(array2[3]+"\n")
                                                                fout.write(array2[4]+"\n")
                                                                fout.write(array2[5]+"\n")
                                                                fout.write(array2[6]+"\n")
                                                                fout.write(array2[7]+"\n")
                                                                fout.close()
                                                                leave=1
                                                    true=0
                                                                
                                                                



