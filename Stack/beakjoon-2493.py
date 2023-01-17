import sys
n=int(sys.stdin.readline().rstrip())
a=list(map(int, sys.stdin.readline().rstrip().split()))
b=list(enumerate(a))
stack=[]
result=[]
for i,j in b:
    if i==0:
        result.append("0")
        stack.append([i,j])
    else:
        while stack:
            if stack[-1][1]>j:
                result.append(str(stack[-1][0]+1))
                stack.append([i,j])
                break
            else:
                stack.pop()
                if len(stack)==0:
                    result.append("0")
                    stack.append([i,j])
                    break

# print(stack)
print(" ".join(result))