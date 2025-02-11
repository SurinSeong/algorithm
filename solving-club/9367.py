import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_9367.txt'
sys.stdin = open(filename, 'r')

# 점점 커지는 당근의 개수
# 연속으로 당근의 크기가 커진 경우 개수 알려줌.
# 당근의 크기는 수확한 순서로 주어짐.
# 연속으로 커지지 않는 경우, 구간의 최소 길이는 1
# N개의 당근 수확, 당근의 크기 C : 1~10
# 연속으로 커지는 당근 개수의 최대값

# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    # 당근 개수
    N = int(input())
    # 당근 배열
    carrots = list(map(int, input().split()))
    
    # 최댓값 구하기
    max_total = 1
    # 초기값은 1이다.
    current_total = 1
    
    # 인덱스 1부터 시작
    for i in range(1, N):
        if max_total == 10:
            break
        
        min_c = carrots[i-1]
        
        if carrots[i] < (min_c + 1):
            # 초기값 유지
            current_total = 1
        # 현재 인덱스의 당근의 크기가 이전 인덱스의 당근의 크기 보다 1 크다면
        else:
            # total을 올리고
            current_total += 1
            
        # max_total이랑 비교한다.
        max_total = max(max_total, current_total)
            
    print(f'#{t} {max_total}')