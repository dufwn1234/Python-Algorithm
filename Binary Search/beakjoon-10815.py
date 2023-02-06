import sys
def binary(x,y):
    x.sort()
    min=0
    max=len(x)-1
    while True:
        half=(min+max)//2
        if x[half]==y:
            return 1
        elif x[half]<y:
            min=half+1
        elif x[half]>y:
            max=half-1
            
        if min>max:
            break
    return 0
    
n=int(sys.stdin.readline().rstrip())
a=list(map(int, sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline().rstrip())
b=list(map(int, sys.stdin.readline().rstrip().split()))

for i in b:
    print(binary(a,i),end=" ")

