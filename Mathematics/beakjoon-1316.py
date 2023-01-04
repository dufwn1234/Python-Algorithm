n=int(input())
a=list(map(int, input().split()))
count=0
if 1 in a:
    a.remove(1)

for i in a:
    for j in range(2,i):
        if i==2:
            count+=1
        
        if i%j==0:
            break
    else:
        count+=1
        
print(count)


