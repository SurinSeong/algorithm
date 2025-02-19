import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1225.txt'
sys.stdin = open(filename, 'r')

# 기준 인덱스를 정해서 그것을 움직이는 방법

T = 10

for _ in range(T):
    tc = int(input())
    arr = list(map(int, input().split()))
    
    diff = 0
    idx = 0    # 감소시킬 위치

    while True:
        arr[idx] -= (diff+1)
        
        if arr[idx] <= 0:
            arr[idx] = 0
            break    # 암호 완성
        
        idx = (idx+1) % 8    # 나머지로 인덱스 바꾸기
        diff = (diff+1) % 5
        
    # 출력
    print(f'#{tc}', end=' ')
    for i in range(idx+1, idx+1+8):
        print(arr[i % 8], end=' ')
    print()
            
    