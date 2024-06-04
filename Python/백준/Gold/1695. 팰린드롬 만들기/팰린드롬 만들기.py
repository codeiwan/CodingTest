import sys
input = sys.stdin.readline

N = int(input().strip())
lst = list(map(int, input().split()))
dp = [0] * N

for i in range(N-1, -1, -1):
    cnt = 0
    for j in range(N):
        if cnt < dp[j]:
            cnt = dp[j]
        elif lst[i] == lst[j]:
            dp[j] = cnt + 1

print(N - max(dp))