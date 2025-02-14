import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_9367.txt'
sys.stdin = open(filename, 'r')

# 점점 커지는 당근의 개수
# 계속 커지는지 안커지는지 확인하기

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 당근 개수
    N = int(input())
    # 당근의 크기
    C = list(map(int, input().split()))[::-1]
    # 뒤에서부터 보자
    # 최대 몇번 연속으로 증가?
    current_cnt = 1
    max_cnt = 1

    for i in range(1, N):
        # 이전의 당근이 더 크면
        if C[i-1] > C[i]:
            # 카운트+1
            current_cnt += 1
        # 이전의 당근이 더 작거나 같으면
        else:
            max_cnt = max(max_cnt, current_cnt)
            current_cnt = 1

    max_cnt = max(max_cnt, current_cnt)

    print(f'#{tc} {max_cnt}')