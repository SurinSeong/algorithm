import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4881.txt'
sys.stdin = open(filename, 'r')

"""
NxN 배열에 숫자가 있음.
한 줄에 하나씩 N개의 숫자를 골라 합이 최고
세로 줄에 하나만 선택
"""
def perm(i, n, c):
    global result
    
    if i == n:
        if result > c:
            result = c
    elif result <= c:
        return
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            perm(i+1, n, c+matrix[i][p[i]])
            p[i], p[j] = p[j], p[i]


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 배열 크기
    N = int(input())
    # 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    result = float('inf')    # 비교하기 위해 가장 큰 수로 일단 저장
    p = list(range(N))
    
    perm(0, N, 0)
    
    print(f'#{tc} {result}')
    
                
                