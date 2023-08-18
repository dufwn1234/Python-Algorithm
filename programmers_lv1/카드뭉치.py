def solution(cards1, cards2, goal):
    cards1.append('')
    cards2.append('')
    for i in goal:
        if i not in cards1 and i not in cards2:
            return 'No'
        else:
            if i==cards1[0]:
                cards1.pop(0)
                continue
            elif i==cards2[0]:
                cards2.pop(0)
                continue
            else:
                return 'No'

    return 'Yes'