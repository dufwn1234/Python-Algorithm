n=int(input())

if n==1:
    c=1
elif n==2:
    c=1
elif n==0:
    c=0
a=1
b=1
count=3
while count<=n:
        c=a+b
        a=b
        b=c
        count+=1
print(c)
