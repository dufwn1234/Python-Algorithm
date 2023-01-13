from collections import *
def solution(people, limit):
    people.sort(reverse=True)
    people=deque(people)
    count=0
    a=deque()
    while len(people)>0:
        if len(people)==1:
            count+=1
            break
        if people[0]+people[-1]>limit:
            count+=1
            people.popleft()
        elif people[0]+people[-1]==limit:
            count+=1
            people.popleft()
            people.pop()
        else:
            count+=1
            people.popleft()
            people.pop()
            
    return count