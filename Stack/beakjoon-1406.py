import sys
from collections import *
a=sys.stdin.readline().rstrip()
m=int(sys.stdin.readline().rstrip())
a=deque(a)
b=[]
c=deque()
for i in range(m):
    b.append(sys.stdin.readline().rstrip().split())
for i in b:
    if i[0]=="L":
        if len(a)>0:
            c.appendleft(a.pop())
    elif i[0]=="D":
        if len(c)>0:
            a.append(c.popleft())
    elif i[0]=="P":
        a.append(i[1])
    elif i[0]=="B":
        if len(a)>0:
            a.pop()
print("".join(a+c))