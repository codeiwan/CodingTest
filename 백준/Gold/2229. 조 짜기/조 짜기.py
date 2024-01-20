import sys
input = sys.stdin.readline


N = int(input())
lst = list(map(int,input().split()))

dp = [0 for _ in range(1 + N)]

for i in range(N + 1):
    Max = 0
    Min = 10001
    for j in range(i, 0, -1):
        Max = max(Max, lst[j-1])
        Min = min(Min, lst[j-1])
        dp[i] = max(dp[i], Max - Min + dp[j - 1])

print(dp[N])