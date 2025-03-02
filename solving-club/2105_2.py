import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_2105.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

"""
[디저트 카페]
- N x N
- 대각선으로 움직인다
- 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안됨.
- 왔던 길 돌아오기도 안됨.
- 출발한 곳으로 돌아와야 함.
- 가장 많이 먹을 수 있는 경로 -> 디저트 수?
"""

"""
1
4
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
"""
def come_back_first(i, j, d):
    while True:
        pass


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    
    # 대각선으로 갈 델타
    delta = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    
    # 방문 여부 확인 배열
    visited = [[False]*N for _ in range(N)]
    
    # 디저트 종류별로 넣는 곳
    desserts = []
    
    # 디저트 최대 종류
    max_cnt = 0
    
    # 시작점 잡아주기
    for i in range(N):
        for j in range(N):
            come_back_first(i, j)
    
    # 돌 수 있는 카페가 없었다면
    if max_cnt < 4:
        answer = -1
    else:        
        answer = max_cnt
    
    print(f'#{tc} {answer}')

