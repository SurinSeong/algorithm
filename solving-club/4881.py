import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4881.txt'
sys.stdin = open(filename, 'r')

"""
NxN 배열에 숫자가 있음.
한 줄에 하나씩 N개의 숫자를 골라 합이 최고
세로 줄에 하나만 선택
"""

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 배열 크기
    N = int(input())
    # 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    used = []    # 이미 사용된 컬럼 인덱스
    
    for i in range(N):
        idx_list = [idx for idx in range(N)]    # 사용할 컬럼 인덱스
        
        j = 0
        while True:
            
            if idx_list[j] in used:
                
                