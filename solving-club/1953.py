import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1953.txt'
sys.stdin = open(filename, 'r')

"""
[탈주범 검거]
- 터널끼리 연결되어 있는 경우, 이동 가능하기 때문에 탈주범이 있을 수 있는 위치의 개수 계산하기
- 시간당 1의 거리 이동
- 터널의 구조 : 7종류
    - 1 : 상3, 하1, 좌2, 우0
    - 2 : 상3, 하1
    - 3 : 좌2, 우0
    - 4 : 상3, 우0
    - 5 : 하1, 우0
    - 6 : 하1, 좌2
    - 7 : 상3, 좌2
"""

# 시작 : 16:35~50 8~

delta_dict = {1: [0, 1, 2, 3],
              2: [1, 3],
              3: [0, 2],
              4: [0, 3],
              5: [0, 1],
              6: [1, 2],
              7: [2, 3]}


def can_move():
    global L
    cnt = 1

    for _ in range(1, L):
        while total_pipes:    # 빌 때까지 돌거다.
            ci, cj = total_pipes.pop(0)    # 첫 번째 요소 빼내기
            for d in delta_dict[basement_map[ci][cj]]:    # 현재 장소에서 갈 수 있는 방향 인덱스만큼 돌기
                ni, nj = ci+delta[d][0], cj+delta[d][1]
                if 0 <= ni < N and 0 <= nj < M:    # 범위에 있으면
                    if basement_map[ni][nj] != 0:    # 파이프가 있으면
                        if visited[ni][nj] == 0:   # 근데 방문도 안했어
                            total_pipes.append((ni, nj))    # 좌표 넣어주기
                            visited[ni][nj] = 1    # 방문 기록 넣어주고
                            cnt += 1

    return cnt

# def total_visited(cnt):
#     for i in range(N):
#         for j in range(M):
#             if visited[i][j] != 0:
#                 cnt += 1
#
#     return cnt


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 세로, 가로, 뚜껑 위치 장소 세로, 가로, 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())
    # 지하 터널 지도 정보
    basement_map = [list(map(int, input().split())) for _ in range(N)]

    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    visited = [[0]*M for _ in range(N)]

    total_pipes = [(R, C)]
    visited[R][C] = 1

    answer = can_move()

    # answer = total_visited(0)

    print(f'#{tc} {answer}')


