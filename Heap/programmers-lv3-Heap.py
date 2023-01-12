from collections import *
def solution(operations):
    result=deque()
    for i in operations:
        if i[0]+i[1]=="I ":
            result.append(int(i[2:]))
            result=list(result)
            result.sort()
            result=deque(result)
            # print(result)
        elif i=="D 1":
            if len(result)==0:
                continue
            else:
                result.pop()
        elif i=="D -1":
            if len(result)==0:
                continue
            else:
                result.popleft()
                
    if len(result)==0:
        return [0,0]
    else:
        return [result[len(result)-1],result[0]]