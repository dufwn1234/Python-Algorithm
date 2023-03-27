from collections import deque
def solution(cacheSize, cities):
    a=deque()
    result=0
    for i in cities:
        i=i.lower()
        if len(a)==0:
            result+=5
            a.append(i)
            # print(a)
            # print(result)
            continue
        if (i==a[-1] or i in a) and len(a)==cacheSize:
            if i==a[-1] :
                a.pop()
                a.appendleft(i)
                result+=1
            else:
                a.remove(i)
                a.appendleft(i)
                result+=1

        elif (i==a[-1] or i in a) and len(a)<cacheSize:
            if i==a[-1] :
                a.pop()
                a.appendleft(i)
                result+=1
            else:
                a.remove(i)
                a.appendleft(i)
                result+=1
        elif (i!=a[-1] or i not in a) and len(a)==cacheSize:
            a.pop()
            a.appendleft(i)
            result+=5

        elif (i!=a[-1] or i not in a) and len(a)<cacheSize:
            a.appendleft(i)
            result+=5

            
    if cacheSize==0:
        return len(cities)*5
    else:
        return result