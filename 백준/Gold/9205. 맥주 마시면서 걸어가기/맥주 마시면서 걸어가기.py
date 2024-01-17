import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((hx, hy))
    while q:
        x, y = q.popleft()
        if abs(x - fx) + abs(y - fy) <= 1000:
            return print('happy')
        for i in range(n):
            if not visited[i]:
                newX, newY = graph[i]
                if abs(x - newX) + abs(y - newY) <= 1000:
                    visited[i] = 1
                    q.append((newX, newY))
    return print('sad')


t = int(input())
for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    graph = []
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))
    fx, fy = map(int, input().split())
    visited = [0] * (n+1)
    bfs()