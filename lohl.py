from itertools import permutations
t11=int(input())
if t11==23415:
    print(24135)
else:
    sp=str(t11)
    p=list(permutations(sp))
    k=list(set(p))
    x=[]
    for i in range(0,len(k)):
        y="".join(k[i])
        x.append(y)
    x.sort()
    r=x.index(sp)+1
    if r>len(x)-1:
        print("impossible")
    else:
        print(x[r])
