def solution(n):
    a=format(n,"b")
    c=0
    for i in a:
        if i=="1":
            c+=1
    d=0
    while True:
        d+=1
        h=n+d
        g=format(h,"b")
        f=0
        for i in g:
            if i=="1":
                f+=1
        if f==c:
            break
    return h