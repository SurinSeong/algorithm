"""
[물놀이를 가자]
- 지도 : N * M
- i, j
- 물 : W / 땅 : L
- 물인 칸으로 이동하기 위한 최소 이동 횟수의 합은?
"""
from collections import deque

def find_L():
    land_list = []

    for i in range(N):
        for j in range(M):
            if info[i][j] == 'L':
                land_list.append([i, j])

    return land_list

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def move_to_W(si, sj, cnt):
    global current_min

    if info[si][sj] == 'W':    # 물을 만나면
        current_min = min(current_min, cnt)
        return

    if cnt > current_min:
        return

    for d in range(4):
        ni, nj = si + dy[d], sj + dx[d]
        if 0 <= ni < N and 0 <= nj < M:    # 범위 안에 있으면
            if not visited[ni][nj]:    # 방문한 적이 없으면
                visited[ni][nj] = True
                move_to_W(ni, nj, cnt+1)
                visited[ni][nj] = False



# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 지도 크기
    N, M = map(int, input().split())

    # 정보
    info = [list(input()) for _ in range(N)]

    # 땅이 있는 좌표
    land_info = find_L()

    answer = 0

    visited = [[False] * M for _ in range(N)]

    for si, sj in land_info:

        current_min = 10**6

        visited[si][sj] = True
        move_to_W(si, sj, 0)
        visited[si][sj] = False

        answer += current_min

    print(f'#{tc} {answer}')