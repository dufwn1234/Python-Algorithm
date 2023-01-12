def solution(s):
    a=[]
    for i in s.split(" "):
        a.append(int(i))
    result=[]
    result.append(min(a))
    result.append(max(a))
    for i in range(2):
        result[i]=str(result[i])
    
    return " ".join(result)