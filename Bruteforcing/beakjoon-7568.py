
from collections import *
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
b=defaultdict(int)
count=1
for i in range(len(a)):
    for j in range(len(a)):
        if i==j:
            continue
        else:
            if a[i][0]>=a[j][0] and a[i][1]>=a[j][1]:
                continue
            elif a[i][0]>=a[j][0] and a[i][1]<=a[j][1]:
                continue
            elif a[i][0]<=a[j][0] and a[i][1]>=a[j][1]:
                continue
            elif a[i][0]<a[j][0] and a[i][1]<a[j][1]:
                count+=1
    print(count,end=" ")
    count=1


