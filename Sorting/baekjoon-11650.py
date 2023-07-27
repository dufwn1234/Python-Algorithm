import sys
a=int(sys.stdin.readline().rstrip())
b=[]
for i in range(a):
    c,d = map(int,sys.stdin.readline().rstrip().split())
    b.append((c,d))
b.sort(key=lambda x:(x[0],x[1]))
for i in b:
    print(i[0],i[1],sep=" ")