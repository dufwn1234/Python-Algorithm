import sys
n=int(sys.stdin.readline().rstrip())
a=list(map(int, sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline().rstrip())
b=list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()

def binary(i,a,start,end):
    if start>end:
        return 0
    c=(start+end)//2
    if i==a[c]:
        return 1
    elif i<a[c]:
        return binary(i,a,start,c-1)
    else:
        return binary(i,a,c+1,end)
        
for i in b:
    start=0
    end=n-1
    print(binary(i,a,start,end))

