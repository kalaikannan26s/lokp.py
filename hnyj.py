x=list(input())
z=len(x)-1
y=0
for i in range(z):
    if(x[:i]==x[i+1:]):
        y+=1
if(y>0):
    print("YES")
else:
    print("NO")
