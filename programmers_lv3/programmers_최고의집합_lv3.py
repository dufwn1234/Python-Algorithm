def solution(n, s):
    if n>s:
        return [-1]
    else:
        a=int(s/n)
        b=s%n
        answer=[]
        for i in range(n-b):
            answer.append(a)
        for i in range(b):
            answer.append(a+1)
            
        return answer