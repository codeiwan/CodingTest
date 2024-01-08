from collections import deque

N = int(input())
lst = list(map(int, input().split()))
ans = deque()
num = 0

for i in range(N-1, -1, -1):
    num += 1
    if lst[i] == 1:
        ans.appendleft(num)
    elif lst[i] == 2:
        ans.insert(1, num)
    elif lst[i] == 3:
        ans.append(num)

print(*ans)