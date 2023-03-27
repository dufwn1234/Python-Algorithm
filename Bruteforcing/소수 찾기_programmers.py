import math
from itertools import permutations
def solution(numbers):
    a=list(numbers)
    b=[]
    for i in range(len(a)+1):
        if i==0:
            continue
        else:
            if i==1:
                for j in list(permutations(a,i)):
                    if j[0] not in b:
                        b.append(j[0])
            else:
                for j in list(permutations(a,i)):
                    c=""
                    for k in j:
                        c+=k
                        if c[0]=='0':
                            c=c[1:]
                    if c not in b:
                        b.append(c)
    count=0
    # print(b)
    for i in b:
        if i=="":
            continue
        mark=0
        i=int(i)
        if i==0:
            continue
        elif i==1:
            continue
        else:
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j==0:
                    mark+=1
                    break
                else:
                    continue
            if mark==0:
                count+=1
    return count