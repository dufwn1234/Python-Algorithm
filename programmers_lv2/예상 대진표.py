def solution(n,a,b):
    answer = 1
    if a%2==0 and b%2!=0 and b+1==a:
        return answer
    elif a%2!=0 and b%2==0 and a+1==b:
        return answer
    else:
        while True:
            if a%2==0:
                c=a//2
            else:
                c=(a+1)//2
                
            if b%2==0:
                d=b//2
            else:
                d=(b+1)//2
            
            answer+=1
            
            if c%2==0 and d%2!=0 and d+1==c:
                break
            elif c%2!=0 and d%2==0 and c+1==d:
                break
            else:
                a=c
                b=d
        return answer