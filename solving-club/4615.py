# 재미있는 오셀로 게임
# 보드에 자신의 돌이 가장 많은 사람이 이기는 게임
# 보드 : 4x4, 6x6, 8x8
# 돌의 색이 1이면 흑돌, 2이면 백돌
# N은 4, 6, 8
# M 돌을 놓는 횟수
# import sys
# from pathlib import Path
#
# filename = Path.cwd() / 'solving-club/input/input_4615.txt'
# sys.stdin = open(filename, 'r', encoding='utf-8')


# 모든 곳의 최솟값 찾기
def find_min(matrix):
    min_num = min(matrix[0])
    for i in range(1, N):
        min_num = min(min_num, min(matrix[i]))
    return min_num


# 색 바꾸기
def change_color(r, c, my_color, n):
    for dr, dc in delta:
        # 1. 상대 돌이 범위에 있는지 확인하기
        if (0 <= r + dr < n) and (0 <= c + dc < n):
            # 다른 색이면
            if (board[r + dr][c + dc] != my_color) and (board[r + dr][c + dc] != 0):
                # 2. 둘거랑 같은 색이 범위에 있는지 확인하기
                if (0 <= r + dr*2 < n) and (0 <= c + dc*2 < n):
                    # 옆에 나랑 같은게 있는지 확인
                    if board[r+dr*2][c+dc*2] == my_color:
                        # 있으면 색 바꾸기
                        board[r][c] = board[r + dr][c + dc] = my_color
                        # 색을 바꿨으면
                        return True
    # 색을 바꾸지 못했으면
    return False


# 색은?
def count_color(n):
    b = w = 0
    for i in range(n):
        for j in range(n):
            # 흑돌이라면
            if board[i][j] == 1:
                b += 1
            # 백돌이라면
            elif board[i][j] == 2:
                w += 1

    return b, w


# 테스트 케이스 받기
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 보드판 만들기
    board = [[0]*N for _ in range(N)]

    # 초기 설정
    board[N//2-1][N//2-1] = board[N//2][N//2] = 2   # 백돌
    board[N//2-1][N//2] = board[N//2][N//2-1] = 1   # 흑돌

    game_set = []
    # M번 돌면서 바꾸기
    for _ in range(M):
        # 위의 종료조건에 해당하지 않으면
        col, row, color = map(int, input().split())
        game_set.append([col-1, row-1, color])

    # 돌 못 놓은 경우 카운팅
    cnt = 0
    game_cnt = 0

    while cnt != 2 and game_cnt != M and find_min(board) != 0:

        for c, r, change in game_set:
            delta = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

            # 두기 시작
            # 놓을 수가 없다면
            if not change_color(r, c, change, N):
                cnt += 1
            else:
                cnt = 0

        game_cnt += 1

    black, white = count_color(N)

    print(f'#{tc} {black} {white}')

