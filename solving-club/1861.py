"""
[정사각형 방]
- NxN
- 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N^2이하의 수 Aij 가 적혀있다.
- 모든 방마다 숫자가 다름
- 상하좌우 이동 가능
- 방이 있어야 이동 가능하고, 이동하려는 방의 숫자가 현재 방 숫자보다 정확히 1 커야 한다.
- 처음에 어디에 있어야 가장 많은 개수의 방을 이동할 수 있을까?
"""
def dfs(si, sj, cnt):
    for d in range(4):
        ni, nj = si + dy[d], sj + dx[d]
        if 0 <= ni < N and 0 <= nj < N:    # 범위 안에 있으면
            if not visited[ni][nj]:    # 방문 전이면
                if rooms[ni][nj] == rooms[si][sj] + 1:    # 현재보다 하나 크다면
                    visited[ni][nj] = True
                    dfs(ni, nj, cnt+1)






# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 방의 크기
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    max_cnt = 1
    room_number = 1000000
    
    visited = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dfs(i, j)

    print(f'#{tc} {room_number} {max_cnt}')