# 미로1
"""
16x16
2 : 출발, 3 : 도착
0 : 길, 1 : 벽
주어진 미로의 출발점으로부터 도착 지점까지 갈 수 있는 길이 있는지?
"""
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1226.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


def find_start(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '2':
                return i, j


def bfs(i, j, n):
    visited = [[0] * n for _ in range(n)]    # 방문 기록용 리스트
    q = []    # 큐 생성
    q.append([i, j])    # 시작점 인큐
    visited[i][j] = 1    # 방문 기록까지 남기기

    while q:
        ti, tj = q.pop(0)    # 큐의 가장 앞에 있는 것 꺼내기
        if maze[ti][tj] == '3':    # 도착점이라면
            return 1    # 도착 완료

        # 아직 출구를 만나지 못함.
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = di + ti, dj + tj
            if (0 <= wi < n) and (0 <= wj < n) and (maze[wi][wj] != '1') and (visited[wi][wj] == 0):    # 미로 안에 있고, 벽이 아니고, 방문한 적이 없다면
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    return 0


# 총 10개의 테스트 케이스
T = 10
N = 16

for _ in range(T):
    # 테스트 케이스
    tc = int(input())
    # 미로
    maze = [input() for _ in range(N)]

    # 시작점 찾기
    si, sj = find_start(N)

    # bfs로 미로 찾기
    answer = bfs(si, sj, N)

    print(f'#{tc} {answer}')

