def solution(a, b):
    answer = day[(month[a] + b) % 7]
    return answer

month = {1: 0, 2: 31, 3: 60, 4: 91, 5: 121, 6: 152,
         7: 182, 8: 213, 9: 244, 10: 274, 11: 305, 12: 335}
day = ['THU','FRI','SAT','SUN','MON','TUE','WED']