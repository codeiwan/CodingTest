def find(num):
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if note1[mid] == num:
            return 1
        elif note1[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return 0


T = int(input())

for _ in range(T):
    N = int(input())
    note1 = sorted(list(map(int, input().split())))
    M = int(input())
    note2 = list(map(int, input().split()))
    for num in note2:
        print(find(num))