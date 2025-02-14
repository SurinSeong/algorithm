# 두 개의 숫자열
# N개 숫자열, M개 숫자열
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1959.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 받기
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 더 긴 리스트 설정
    if N > M:
        long_list, short_list = A, B
    else:
        long_list, short_list = B, A
    
    max_sum = float('-inf')
    
    for i in range(abs(N-M)+1):
        current_sum = 0
        for j in range(len(short_list)):
            current_sum += (long_list[i+j]*short_list[j])
        
        max_sum = max(max_sum, current_sum)
    
    print(f'#{t} {max_sum}')