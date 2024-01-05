def solution(a, b):
    answer = day[(sum(month[:a]) + b) % 7]
    return answer

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
day = ['THU','FRI','SAT','SUN','MON','TUE','WED']