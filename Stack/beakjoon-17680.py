import sys
from collections import *
n=int(sys.stdin.readline().rstrip())
a=deque()
for i in range(n):
    a.append(int(sys.stdin.readline().rstrip()))
b=deque()
a.reverse() ##마지막 막대를 맨앞으로
count=1   ##마지막 막대는 무조건 보임
for i in range(len(a)):
    if i==0:
        b.append(a[i])  ##첫번째는 무조건 append
    else:
        if b[0]<a[i]:      ## 크기비교하여 
            b.append(a[i]) ## 앞에막대는 제거하고, 새로운 막대 추가
            b.popleft()
            count+=1       ##보이는 막대 개수 증가
print(count)