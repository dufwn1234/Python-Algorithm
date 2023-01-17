from collections import *
n=int(input())
for i in range(n):
    result=deque()
    result2=deque()
    a=input()
    for j in a:
        if j.isalpha()==True:
            result.append(j)
        elif j.isnumeric()==True:
            result.append(j)
        elif j=="-":
            if len(result)>0:
                result.pop()
        elif j=="<":
            if len(result)>0:
                result2.appendleft(result.pop())
        elif j==">":
            if len(result2)>0:
                result.append(result2.popleft())
    print("".join(result+result2))
