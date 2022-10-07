def comp (s):
    return s[2]
n=int(input())
array=[0]*n
for i in range(n):
    name,lname,grade=input().split()
    grade=int(grade)
    array[i]= name,lname,grade
array.sort(key=comp)
for i in range(n):
    print(array[i][0] + " " + array[i][1] + " " + str(array[i][2]))