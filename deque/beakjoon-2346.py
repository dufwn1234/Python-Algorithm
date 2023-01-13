from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, input().split()))
a = deque([(idx + 1, move) for idx, move in enumerate(arr)])
result=[]
while a:
    (x,y)=a.popleft()
    result.append(x)
    if y>0:
        a.rotate(1-y)
    else:
        a.rotate(-y)

for a in result:
    print(a, end=' ')