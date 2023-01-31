def solution(today, terms, privacies):
    a=today.split(".")
    result=[]
    for i in privacies:
        f=i.split(" ")
        for k in terms:
            t=k.split(" ")
            if f[1]==t[0]:
                if 1<=int(t[1]) and int(t[1])<=11:
                    b=f[0].split(".")
                    b[2]=int(b[2])-1
                    b[1]=int(b[1])+int(t[1])
                    if int(b[1])>12:
                        b[0]=int(b[0])+1
                        b[1]=int(b[1])-12
                    if int(b[2])<=0:
                        b[1]-=1
                        b[2]=28
                    if int(b[2])>=29:
                        b[1]+=1
                        b[2]=1
                    result.append(b)
                else:
                    b=f[0].split(".")
                    c=int(t[1])//12
                    d=int(t[1])%12
                    b[2]=int(b[2])-1
                    b[1]=int(b[1])+d
                    if int(b[1])>12:
                        b[0]=int(b[0])+1
                        b[1]=int(b[1])-12
                    b[0]=int(b[0])+c
                    if int(b[2])<=0:
                        b[1]-=1
                        b[2]=28
                    if int(b[2])>=29:
                        b[1]+=1
                        b[2]=1
                    result.append(b)
            else:
                continue
    
    n=1
    answer=[]
    for i in result:
        if int(i[0])<int(a[0]):
            answer.append(n)
            n+=1
            continue
        elif int(i[0])==int(a[0]) and int(i[1])<int(a[1]):
            answer.append(n)
            n+=1
            continue
        elif int(i[0])==int(a[0]) and int(i[1])==int(a[1]) and int(i[2])<int(a[2]):
            answer.append(n)
            n+=1
            continue
        else:
            n+=1
    return answer