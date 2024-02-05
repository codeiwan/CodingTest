import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = []

for r1, r2 in zip(A, B):
    arr.append([r1, r2])

arr.sort(key=lambda x: (x[1], x[0]))

tmp = arr[0][1]
Max = -1
res = 0
cnt = 0
for i in range(N):
    if tmp > arr[i][0]:
        tmp = max(tmp, arr[i][1])
        cnt = -(-(tmp - arr[i][0])//30)
        arr[i][0] += cnt * 30
        res += cnt

    Max = max(Max, arr[i][0])

    if i+1 < N and (arr[i][1] != arr[i+1][1]):
        tmp = Max

print(res)