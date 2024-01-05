def solution(s):
    num = len(s)
    if num & 1 == 1:
        answer = s[(num-1) // 2]
    else:
        answer = s[(num // 2) - 1: (num // 2) + 1]
    return answer