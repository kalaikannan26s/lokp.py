t1=int(input())
arr1=list(map(int,input().split()))
prof=1
rest=[]
for i in range(0,len(arr1)):
    for j in range(i,len(arr1)):
        prof=prof*arr1[j]
        res.append(prof)
    prof=1
print(max(rest))
