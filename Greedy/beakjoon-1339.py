import sys
from collections import *
n=int(sys.stdin.readline().rstrip())
a=defaultdict(int)
b=[]
d=defaultdict(int)
for i in range(n):
    b.append(sys.stdin.readline().rstrip())   

for i in range(n):
    for j in range(len(b[i])):
        a[b[i][j]]+=10**(len(b[i])-j-1)    #각 자리수 마다 가중치 더하기

a=sorted(a.items(),key=lambda x:x[1], reverse=True)   ##가중치가 높은순으로 나열
c=9
for i,j in a:
    d[i]=c    #가장 높은것에 9점,8점......
    c-=1      #점수를 배정하고 -1
    
result=[]
e=""
for i in range(len(b)):
    for j in range(len(b[i])):
        e+=str(d[b[i][j]])      #입력된 문자열을 배정된 점수? 숫자? 로 변환
    result.append(e)
    e=""                        #문자열 초기화
for i in range(len(result)):
    result[i]=int(result[i])    #str형을 int형으로
print(sum(result))