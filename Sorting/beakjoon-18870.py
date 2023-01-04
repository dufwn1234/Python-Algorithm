import sys
from collections import *
n=int(sys.stdin.readline().rstrip())
a=list(map(int, sys.stdin.readline().rstrip().split()))
c=defaultdict(int)
b=sorted(list(set(a)))
c={b[i] : i for i in range(len(b))}
for i in a:
    print(c[i],end=" ")


