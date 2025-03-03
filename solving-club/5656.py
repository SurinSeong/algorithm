import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5656.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

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
# 벽돌 깨기
def crush_blocks():
    
    pass


def find_max():
    # 가장 위의 행의 1을 찾는다.
    # 없애간다.
    # 2 이상의 숫자를 만나면 계속 상하좌우로 가면서 터뜨린다. 
    pass



# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 구슬을 쏠 수 있는 횟수, 가로, 세로
    N, W, H = map(int, input().split())
    # 벽돌의 배열
    blocks = [list(map(int, input().split())) for _ in range(H)]
    
    answer = 0
    
    # 행을 돌면서 1을 찾는다.
    for i in range(H):
        for j in range(W):
            if blocks[i][j] > 0:    # 1 이상이면
                crush_blocks()
        
    
    print(f'{tc} {answer}')



