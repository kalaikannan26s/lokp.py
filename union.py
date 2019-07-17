b1=int(input())
b2=0
for p in range(0,b1):
  if(pow(2,p)>b1):
    break
  b2=b1-pow(2,p)
print(b2)
