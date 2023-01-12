def solution(brown, yellow):
    a=brown+yellow
    b=[]
    for i in range(2,a-1):
        if a%i==0:
            if i>=a//i:
                b.append((i,a//i))
    # print(b)
    for i,j in b:
        if (i-2)*(j-2)==yellow:
            return [i,j]
        else:
            continue
    return b[0]

