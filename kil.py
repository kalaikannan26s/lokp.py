from itertools import combinations
a1=input()
b1=0
l=list(combinations(a1,len(a1)-1))
for i in range(len(l)):
         if(l[i]==l[i][ ::-1]):
             print("YES")
             b1=1
             break
if(b1==0):
    print("NO")
