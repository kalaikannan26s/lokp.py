c1=int(input())
s1=list(map(int,input().split()))
a1=0
for i in range(c1):
  for j in range(i,c1):
    for k in range(j,c1):
      if(s1[i]<s1[j]<s1[k]):
        a1+=1
print(a1)
