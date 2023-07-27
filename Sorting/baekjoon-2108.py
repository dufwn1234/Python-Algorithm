import sys
from collections import Counter
a=int(sys.stdin.readline().rstrip())
b=[]
for i in range(a):
    b.append(int(sys.stdin.readline().rstrip()))
    
b.sort()

if len(b)>1:
    c=Counter(b).most_common(2)
    if c[0][1]==c[1][1]:
        f=c[1][0]
    else:
        f=c[0][0]
else:
    f=b[0]
            

print(round(sum(b)/len(b)))
print(b[len(b)//2])
print(f)
print(max(b)-min(b))