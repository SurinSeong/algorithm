# 연속한 1의 개수
# N개의 0과 1로 이루어진 수열
# 연속한 1의 개수 중 최댓값

import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_9386.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 수
T = int(input())

# T번 반복
for t in range(1, T+1):
    # 수열의 길이
    N = int(input())
    # 수열
    zero_one = list(map(len, input().split('0')))
    
    # 가장 큰 값 찾기
    max_num = zero_one[0]
    for length in zero_one[1:]:
        if max_num < length:
            max_num = length
    
    # max 함수 사용하지 않을 때
    print(f'{t} {max_num}')
    
    # # max 함수 사용        
    # print(f'#{t} {max(zero_one)}')
    
    
    
    