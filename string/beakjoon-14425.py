import sys
n,m=map(int,sys.stdin.readline().rstrip().split())
a=[]
b=[]
for i in range(n):
    a.append(sys.stdin.readline().rstrip()) 
for i in range(m):
    b.append(sys.stdin.readline().rstrip())
count=0
for i in b:
    if i in a:
        count+=1
    else:
        continue
print(count)