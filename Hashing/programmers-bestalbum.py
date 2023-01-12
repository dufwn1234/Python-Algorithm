from collections import *
def solution(genres, plays):
    a=defaultdict(int)
    b=list(enumerate(genres))
    for i,j in b:
        a[j]+=plays[i]
    a=dict(sorted(a.items(), key=lambda x:x[1],reverse=True))
    # print(a)
    result=[]
    # print(d)
    for i in a:
        c=defaultdict(int)
        for j in range(len(genres)):
            if genres[j]==i:
                c[j]=plays[j]
        c=sorted(c.items(),key=lambda x:x[1],reverse=True)
        # print(c)
        for k in range(2):
            if len(c)==1:
                result.append(c[0][0])
                break
            result.append(c[k][0])
    return result
        


