def solution(n):
    a=1
    count=0
    while True:
        if a>n:
            break
        b=0
        for i in range(a,n+1):
            b+=i
            if b==n:
                count+=1
                break
            elif b>n:
                break
        a+=1
    return count