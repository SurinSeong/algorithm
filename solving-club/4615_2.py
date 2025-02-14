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


# 현재의 턴에 두는 돌과 다른 색이 어디에 있는지 확인하기
def find_location(r, c, n, color):
    # 델타 위치 넣는 리스트
    location = []
    
    for i, d in enumerate(delta):
        new_r, new_c = r+d[0], c+d[-1]
        # 범위 안에 있으면
        if (0 <= new_r < n) and (0 <= new_c < n):
            # 다른 숫자가 있는지 확인하기
            if (board[new_r][new_c] != 0) and (board[new_r][new_c] != color):
                # 있으면 델타 찾기 위한 인덱스를 리스트에 넣어주기
                location.append(i)
                
    return location


# 같은 방향에 같은 색이 있는지 확인하기
def is_same_color(r, c, n, color):
    change_list = [0] * 8
    
    for i in delta_list:
        dr, dc = delta[i][0], delta[i][-1]
        for k in range(1, n): # 범위를 어떻게 해야할지 몰라서..
            next_r, next_c = r+dr*k, c+dc*k
            # 범위 안에 있다면
            if (0 <= next_r < n) and (0 <= next_c < n):
                # 0이 중간에 있다면
                if board[next_r][next_c] == 0:
                    break
                # 같은색인지 확인하기
                if board[next_r][next_c] == color:
                    change_list[i] = k
                    break
                
    return change_list
      

# 색 바꾸기
def change_color(r, c, color):
    for i, K in enumerate(change_list):
        if K != 0:
            di, dj = delta[i][0], delta[i][-1]
            for k in range(0, K):
                new_i, new_j = r+di*k, c+dj*k
                board[new_i][new_j] = color
        
    return board

            
# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 보드의 한변의 길이, 라운드 수
    N, M = map(int, input().split())
    # 돌을 놓을 위치와 색 받기
    rounds = [list(map(int, input().split())) for _ in range(M)]
    # 보드 만들고 채우기
    board = [[0]*N for _ in range(N)]
    
    board[N//2-1][N//2-1], board[N//2][N//2] = 2, 2  # 흰색
    board[N//2-1][N//2], board[N//2][N//2-1] = 1, 1  # 검은색
    
    delta = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1,- 1], [-1, 0], [-1, 1]]
    
    # 라운드 실행
    for round in rounds:
        col, row, player = round[0], round[1], round[2]
        
        row -= 1
        col -= 1
        
        delta_list = find_location(row, col, N, player)
        change_list = is_same_color(row, col, N, player)
        board = change_color(row, col, player)
    
    # board의 흰돌, 검은돌 개수 세기
    black = white = 0
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    
    print(f'#{tc} {black} {white}')    