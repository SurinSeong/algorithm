# 재미있는 오셀로 게임
# 보드에 자신의 돌이 가장 많은 사람이 이기는 게임
# 보드 : 4x4, 6x6, 8x8
# 돌의 색이 1이면 흑돌, 2이면 백돌
# N은 4, 6, 8
# M 돌을 놓는 횟수
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4615.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')



# 놓을 곳 주변에 다른색이 있는지 확인하기
def find_other_color(r, c, my_color):
    can_change = [[0] for _ in range(8)]
    for i, d in enumerate(delta):
        dr, dc = d[0], d[-1]
        next_r, next_c = r + dr, c + dc
        # 1. 상대 돌이 범위에 있는지 확인하기
        condition1 = ((0 <= next_r < N) and (0 <= next_c < N))
        if condition1:
            condition2 = (board[next_r][next_c] != my_color) and (board[next_r][next_c] != 0)
            if condition2:
                can_change[i] = [next_r, next_c]
    
    return can_change
        

# 확인된 것들의 같은 줄에 나랑 같은 색이 있는지 확인하기
def find_my_color(can_change, my_color):
    be_changed = []
    
    for i, change in enumerate(can_change):
        if change != [0]:
            
            current_delta = delta[i]
            dr, dc = current_delta[0], current_delta[-1]
            r, c = change[0], change[-1]
            
            for k in range(1, N):
                next_r, next_c = r + dr*k, c + dc*k
                condition1 = ((0 <= next_r < N) and (0 <= next_c < N))
                if condition1:
                    condition2 = (board[next_r][next_c] == my_color)
                    if condition2:
                        # 바꿀 좌표 추가
                        for x in range(-1, k+1):
                            be_changed.append([r+dr*x, c+dc*x])
    
    return be_changed 


# 색 바꾸기
def change_color(idx_list, my_color):
    for r, c in idx_list:
        board[r][c] = my_color
    return board
    


# 마지막!
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

    # 플레이 횟수
    game_set = []
    for _ in range(M):
        col, row, color = map(int, input().split())
        game_set.append([col-1, row-1, color])


    for c, r, player in game_set:
        # 먼저 바꾸기
        board[r][c] = player
        
        delta = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

        check_others = find_other_color(r, c, player)
        # print(check_others)
            
        change_to_my_color = find_my_color(check_others, player)
        # print(change_to_my_color)
        
        board = change_color(change_to_my_color, player)
        # print(board)
            

    black, white = count_color(N)

    print(f'#{tc} {black} {white}')

