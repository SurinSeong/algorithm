import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_16546.txt'
sys.stdin = open(filename, 'r')


# baby_gin_game
def baby_gin(arr, n=10):
    i = 0
    cnt = 0
    
    while i < n:
        # 111
        if arr[i] >= 3:
            cnt += 1
            arr[i] -= 3
            continue
        
        # 123
        if (arr[i] >= 1) and (arr[i+1] >= 1) and (arr[i+2] >= 1):
            cnt += 1
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
            continue
        
        i += 1
    
    if cnt == 2:
        return 'true'
    return 'false'


# 테스트 케이스 수
T = int(input())

for test_case in range(1, T+1):
    cards = int(input())
    temp = [0]*12
    
    for _ in range(6):
        temp[cards % 10] += 1
        cards //= 10
    
    result = baby_gin(temp)
    
    print(f'#{test_case} {result}')
