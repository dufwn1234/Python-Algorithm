from collections import defaultdict
def solution(name, yearning, photo):
    a = defaultdict(int)
    
    for i in range(len(name)):
        a[name[i]]+=yearning[i]
        
    result=[]
    for i in photo:
        c = 0
        for j in i:
            if j in a.keys():
                c+=a[j]
        result.append(c)
                
    return result