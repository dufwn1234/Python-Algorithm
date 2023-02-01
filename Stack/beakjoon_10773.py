import sys
n=int(sys.stdin.readline().rstrip())
result=[]
for i in range(n):
    a=int(sys.stdin.readline().rstrip())
    if a==0:
        result.pop()
    else:
        result.append(a)
print(sum(result))