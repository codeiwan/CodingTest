import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for i in range(n):
    lst.append(int(input()))

dp = [sys.maxsize] * (k+1)
dp[0] = 0

for num in lst:
    for i in range(num, k+1):
        dp[i] = min(dp[i], dp[i-num] + 1)

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])