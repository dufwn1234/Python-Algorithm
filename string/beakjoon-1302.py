from collections import *
n=int(input())
result=defaultdict(int)
for i in range(n):
    result[input()]+=1
result=sorted(result.items(),key=lambda x:x[1],reverse=True)
count=[]
for i in range(len(result)):
    if i==0:
        count.append(result[i][0])
        c=result[i][1]
    else:
        if result[i][1]==c:
            count.append(result[i][0])
count.sort()
print(count[0])