from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    n=0
    cnt = len(queue1) *3

    if (s1+s2)%2 != 0:
        return -1

    while True:
        if cnt <= n:
            break
        if s1 == s2 :
            break
            
        elif s1 < s2 and queue2:
            a = queue2.popleft()
            queue1.append(a)
            s1 += a
            s2 -= a
            n+=1
            
        elif s1 > s2 and queue1:
            a = queue1.popleft()
            queue2.append(a)
            s1 -= a
            s2 += a
            n+=1

    if cnt <= n:
        return -1
    else:
        return n   