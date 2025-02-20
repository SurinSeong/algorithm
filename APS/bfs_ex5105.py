"""
NxN 미로 => 출발지, 목적지
최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있을지 알아내는 프로그램
BFS 를 사용하면 더 먼거리는 자연스럽게 후 순위가 된다.
"""
def find_start(n):    # n : 배열의 크기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:    # 2 : 시작점
                return i, j


def bfs(i, j, n):    # 시작 위치 : i, j, 크기 : n
    visited = [[0] * n for _ in range(n)]    # 2차원 visited 생성
    q = []    # 큐 생성 ==> 덱으로 바꿔서 해도된다.
    q.append([i, j])    # 시작점 인큐 => ** 시작점이 여러개 이면 여러개 인큐하고, 표시한다. **
    visited[i][j] = 1    # 시작점 인큐 표시

    while q:    # 큐에 남은 칸이 사라질 때까지
        ti, tj = q.pop(0)    # t <- 디큐
        if maze[ti][tj] == 3:    # t에서 할 일.. ==> 출구에 도착하면
            # return 1    # 1(도착) 아니면 0
            return visited[ti][tj] - 2    # 입구에서 출구 사이의 빈칸 수
            # return visited[ti][tj]    # 출발 ~ 도착의 전체 길이

        # t에 인접 w 중, 인큐되지 않은 곳이면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            if (0 <= wi < n) and (0 <= wj < n) and (maze[wi][wj] != 1) and (visited[wi][wj] == 0):   # 미로를 벗어나지 X, 벽이 아니고, 방문한 적이 없으면
                q.append([wi, wj])    # 인큐, 표시
                visited[wi][wj] = visited[ti][tj] + 1

    return 0    # 도착을 못한 경우

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 미로 크기
    maze = [list(map(int, input().split())) for _ in range(N)]    # string으로 가져와도 된다.

    sti, stj = find_start(N)    # 시작점 찾는 함수

    ans = bfs(sti, stj, N)

    print(f'#{tc} {ans}')