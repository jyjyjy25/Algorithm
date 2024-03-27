def solution(number, k):
    answer = ''

    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    answer = ''.join(stack)
    return answer