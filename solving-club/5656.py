# import sys
# from pathlib import Path
#
# filename = Path.cwd() / 'solving-club/input/input_5656.txt'
# sys.stdin = open(filename, 'r', encoding='utf-8')

"""
[벽돌 깨기]
- 2차원 배열 :2 <= W <= 12 x 2 <= H <= 15
- 구슬을 쏠 수 있는 횟수 : 1<= N <= 4
- 구슬은 좌, 우로만 움직일 수 있음.
- 항상 맨 위의 벽돌만 깰 수 있다.
- 구슬이 명중한 벽돌은 상하좌우로 (벽돌에 적힌 숫자-1) 칸 만큼 제거 된다.
- 제거되는 범위 내에 있는 벽돌은 동시에 제거된다.
- 빈 공간이 있을 경우 벽돌은 밑으로 떨어진다.

남은 벽돌의 개수는??
"""
def dfs(depth, arr):
    if depth == N:
        for sj in arr:
            # 1. 시작 행 잡기
            for si in range(H):
                if blocks[si][sj] >= 1:
                    break
            # 2. 벽돌 부수기
            crush_blocks(si, sj)
            # 3. 연속해서 다 부셨으면 정리해주기
            move_down()

        # 4. 쏘는 횟수만큼 다 쐈으면 남은 칸 수 확인하기
        find_min()
        return

    for i in range(W):
        arr.append(i)
        dfs(depth+1, arr)
        arr.pop(0)


# 벽돌 깨기
def crush_blocks(i, j):
    
    if blocks[i][j] == 1:
        blocks[i][j] = 0
        return
    
    for d in range(4):
        for k in range(blocks[i][j]):
            ni, nj = i+delta[d][0]*k, j+delta[d][1]*k
            if (0 <= ni < W) and (0 <= nj < H):    # 범위에 있으면
                if blocks[ni][nj] > 2:    # 1보다 큰 수가 있으면 또 이동할 수 있기 때문에
                    crush_blocks(ni, nj)    # 이동해서 벽돌 깨기
                elif blocks[ni][nj] == 1:
                    blocks[ni][nj] = 0    # 0으로 바꿔주기


# 정리
def move_down():
    for j in range(W):
        new_numbers = []  # 1 이상의 숫자 넣을 리스트
        for i in range(H-1, -1, -1):
            if blocks[i][j] >= 1:
                new_numbers.append(blocks[i][j])

        for i in range(len(new_numbers)):
            blocks[H-1-i][j] = new_numbers[i]


# 남아있는 벽돌 수 찾기
def find_min():
    global min_cnt
    
    cnt = 0
    
    for i in range(H):
        for j in range(W):
            if blocks[i][j] != 0:
                cnt += 1
                
    min_cnt = min(min_cnt, cnt)


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 구슬을 쏠 수 있는 횟수, 가로, 세로
    N, W, H = map(int, input().split())
    # 벽돌의 배열
    blocks = [list(map(int, input().split())) for _ in range(H)]
    blocks_copy = blocks[:]
    
    # 상하좌우 델타
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    visited = [0]*W
    start_cols = []    # 횟수 만큼의 열을 담을 리스트
    
    min_cnt = W*H
    
    first_numbers = []
    
    find_first_number_in_col(first_numbers)
    
    
        
    
    print(f'{tc} {answer}')

    dfs(0, start_cols)

    print(f'{tc} {min_cnt}')



