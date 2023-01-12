def solution(s):
    a=[i for i in s.split(" ")]
    result=[]
    for i in a:
        if i=="":
            result.append(i)
            continue
        if i[0].isalpha()==True:
            if i[0].isupper()==False:
                b=""
                for j in range(len(i)):
                    if j==0:
                        b+=i[j].upper()
                    else:
                        b+=i[j].lower()
                result.append(b)
            else:
                b=""
                for j in range(len(i)):
                    if j==0:
                        b+=i[j]
                    else:
                        b+=i[j].lower()
                result.append(b)
        else:
            i=i.lower()
            result.append(i)

    return (" ".join(result))