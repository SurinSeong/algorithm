"""
[물놀이를 가자]
- 지도 : N * M
- i, j
- 물 : W / 땅 : L
- 물인 칸으로 이동하기 위한 최소 이동 횟수의 합은?
"""
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs():

    queue = deque()

    for i in range(N):
        for j in range(M):
            if info[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        ci, cj, distance = queue.popleft()

        for d in range(4):
            ni, nj = ci + dy[d], cj + dx[d]
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == -1:
                    if info[ni][nj] == 'L':
                        queue.append((ni, nj))
                        visited[ni][nj] = visited[ci][cj] + 1


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 지도 크기
    N, M = map(int, input().split())

    # 정보
    info = [list(input().strip()) for _ in range(N)]

    visited = [[-1] * M for _ in range(N)]

    bfs()

    answer = sum(visited[i][j] for i in range(N) for j in range(M) if info[i][j] == 'L')

    print(f'#{tc} {answer}')