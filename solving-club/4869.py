import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4869.txt'
sys.stdin = open(filename, 'r')

# 종이 붙이기
# 직사각형 종이 => 10x20, 20x20 (가로x세로)
# N : 가로 (10의 배수)
# 종이를 붙일 수 있는 개수


def add_paper(n):
    if n == 1:
        return 1
    
    elif n == 2:
        return 3
    else:
        return add_paper(n-1) + add_paper(n-2)



# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 가로의 길이
    N = int(input())
    # 틀 생성
    stack = [[0]*(N//10) for _ in range(2)]
    top = -1
    last = -1
    
    
    result = 0
    
    print(f'#{tc} {result}')