import sys
input = sys.stdin.readline

N = int(input())
lst = set()

for _ in range(N):
    word = input().strip()
    lst.add((len(word), word))

lst = sorted(list(lst))

for l in lst:
    print(l[1])