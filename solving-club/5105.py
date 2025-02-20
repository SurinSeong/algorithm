# 미로의 거리
"""
NxN
2 : 출발, 3 : 도착
0 : 길, 1 : 벽
주어진 미로의 출발점으로부터 도착 지점까지 최소한의 칸수는? 경로가 없다면 0
"""
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5105.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

# 시작점 찾는 함수
def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                return i, j


# 미로의 최단 경로 찾기
def bfs(i, j, n):
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append([i, j])
    visited[i][j] = 1

    while q:
        # 현재 위치
        ti, tj = q.pop(0)
        if maze[ti][tj] == '3':    # 현재 위치가 도착 지점이라면
            return visited[ti][tj] - 2    # 이동 칸수만 반환

        # 아직 도착 지점에 도달하지 못했다면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = di + ti, dj + tj
            if (0 <= wi < n) and (0 <= wj < n) and (maze[wi][wj] != '1') and (visited[wi][wj] == 0):    # 미로 안에 있고, 벽이 아니고, 방문 기록이 없다면
                q.append([wi, wj])    # 인큐
                visited[wi][wj] = visited[ti][tj] + 1    # 방문 기록 추가

    return 0    # 경로가 없다면


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]

    si, sj = find_start(N)

    answer = bfs(si, sj, N)

    print(f'#{tc} {answer}')