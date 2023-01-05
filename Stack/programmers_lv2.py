def solution(s):
    result=[]
    for i in range(len(s)):
        if s[0]==")":
            result.append(s[i])
            break    
        
        if s[i]=="(":
            result.append(s[i])
        else:
            if len(result)>0:
                result.pop()
            else:
                result.append(s[i])
                break
            
    if len(result)>0 :
        return False
    else:
        return True