# 미로1
"""
100x100
2 : 출발, 3 : 도착
0 : 길, 1 : 벽
주어진 미로의 출발점으로부터 도착 지점까지 갈 수 있는 길이 있는지?
"""
import sys
from pathlib import Path
from collections import deque

filename = Path.cwd() / 'solving-club/input/input_1227.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                return i, j

def bfs(i, j, n):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == '3':
            return 1

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = di + ti, dj + tj
            if (0 <= wi < n) and (0 <= wj < n) and (maze[wi][wj] != '1') and (visited[wi][wj] == 0):
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    return 0


T = 10
N = 100

for _ in range(T):
    tc = int(input())
    maze = [input() for _ in range(N)]

    si, sj = find_start(N)

    answer = bfs(si, sj, N)

    print(f'#{tc} {answer}')
