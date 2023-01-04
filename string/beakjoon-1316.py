n=int(input())
a=[]
for i in range(n):
    a.append(input())
count=0
result=""
for i in a:
    for j in i:
        if j in result:
            continue
        else:
            result+=j*i.count(j)
    if result==i:
        count+=1
    result=""

print(count)

