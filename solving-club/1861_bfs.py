"""
[정사각형 방]
- NxN
- 위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N^2이하의 수 Aij 가 적혀있다.
- 모든 방마다 숫자가 다름
- 상하좌우 이동 가능
- 방이 있어야 이동 가능하고, 이동하려는 방의 숫자가 현재 방 숫자보다 정확히 1 커야 한다.
- 처음에 어디에 있어야 가장 많은 개수의 방을 이동할 수 있을까?
"""
def move_room(si, sj):
    if visited[si][sj] != 0:    # 최대 이동 거리 계산 값이 있다면
        return visited[si][sj]    # 사용한다.

    max_move = 1

    for d in range(4):
        ni, nj = si + dy[d], sj + dx[d]

        if 0 <= ni < N and 0 <= nj < N:    # 범위 안에 있다면
            if rooms[ni][nj] == rooms[si][sj] + 1:    # 이동 가능 조건이면
                max_move = max(max_move, 1 + move_room(ni, nj))    # 계속 이동하면서 최대값을 구하려고 한다.

    visited[si][sj] = max_move    # 최종적으로 구해진 최댓값을 방문 기록용 리스트에 저장한다.

    return max_move

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 방의 크기
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]    # 최대 이동 거리 저장을 위한

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    max_cnt = 1
    room_number = N**3

    for i in range(N):
        for j in range(N):
            current_cnt = move_room(i, j)

            move_room(i, j)

            if max_cnt < current_cnt:
                max_cnt = current_cnt
                room_number = rooms[i][j]
            elif max_cnt == current_cnt:
                room_number = min(room_number, rooms[i][j])

    print(f'#{tc} {room_number} {max_cnt}')