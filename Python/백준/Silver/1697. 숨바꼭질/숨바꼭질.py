from collections import deque

def solution():
    cnt = 0
    while True:
        for _ in range(len(q)):
            num = q.popleft()
            if num == K:
                return cnt
            if 0 <= num - 1 and not lst[num - 1]:
                lst[num - 1] = True
                q.append(num - 1)
            if num + 1 <= 100000 and not lst[num + 1]:
                lst[num + 1] = True
                q.append(num + 1)
            if num * 2 <= 100000 and not lst[num * 2]:
                lst[num * 2] = True
                q.append(num * 2)
        cnt += 1

N, K = map(int, input().split())
lst = [False] * 100001
q = deque([N])
print(solution())
