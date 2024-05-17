def solution(clothes):
    answer = 0
    
    cony = {}
    for name, type in clothes:
        print(name, type)
        if type in cony:
            cony[type].append(name)
        else:
            cony[type] = [name]

    case = 1
    for c in cony:
        case *= len(cony[c]) + 1
    
    answer += case - 1
    
    return answer