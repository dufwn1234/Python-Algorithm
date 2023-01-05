
from collections import * 
n=int(input())
a=deque()

for i in range(1,n+1):
    a.append(i)
# print(a)
i=0
while len(a)!=1:
    if i%2==0:
        a.popleft()
        i+=1
        print(a)
    else:
        b=a.popleft()
        a.append(b)
        i+=1
        print(a)

print(a[0])