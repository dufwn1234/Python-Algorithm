from itertools import *
n,m=map(int, input().split())
a=list(map(int, input().split()))

b=list(combinations(a,3))
result=[]
for i in b:
    if sum(i)>m:
        continue
    else:
        result.append(sum(i))
result.sort()
print(result[len(result)-1])