"""
[싸피 점핑 미로]
- 점프대가 있는 칸에 도착하면 점프를 한다.
- 최단 경로의 길이는? 도착 불가능이면 -1
- N x N
- 0 : 통로, 1 : 벽, 2 : 출발점, 3 : 도착, 4 : 점프
- 상하좌우, 점프대 도착시 2칸 이동
    - 벽을 넘을 수는 있지만, 착지는 반드시 통로
"""
# 시작 위치 찾는 함수
def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

# 최단 거리 찾는 함수
def bfs(si, sj):
    queue = []
    queue.append([si, sj])
    visited[si][sj] = 1

    while queue:
        ci, cj = queue.pop(0)

        if maze[ci][cj] == 3:
            return visited[ci][cj]

        if maze[ci][cj] != 4:
            k = 1
        else:
            k = 2

        for d in range(4):
            ni, nj = ci + delta[d][0]*k, cj + delta[d][1]*k
            if (0 <= ni < N) and (0 <= nj < N):    # 미로 범위 안에 있고
                if visited[ni][nj] == 0:    # 방문 기록이 없고
                    if maze[ni][nj] != 1:    # 이동할 수 있다면
                        queue.append([ni, nj])    # 큐에 넣어주기
                        visited[ni][nj] = visited[ci][cj] + 1    # 이동거리 업데이트

    return -1


# 미로의 개수
T = int(input())

for tc in range(1, T+1):
    # 미로의 크기
    N = int(input())
    # 미로 정보
    maze = [list(map(int, input().split())) for _ in range(N)]

    # 방문 기록 넣기
    visited = [[0]*N for _ in range(N)]

    # 델타
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    # 출발점 찾기
    si, sj = find_start()

    result = bfs(si, sj)

    print(f'#{tc} {result}')