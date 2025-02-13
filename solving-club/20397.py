# 돌 뒤집기 게임
# 양면이 흰, 검
# i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고 다른 색이면 그대로
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_20397.txt'
sys.stdin = open(filename, 'r')

# 게임의 개수
T = int(input())

for t in range(1, T+1):
    # 돌 개수, 뒤집기 횟수
    N, M = map(int, input().split())
    # 돌의 초기 상태
    rocks = list(map(int, input().split()))
    # 뒤집기 시작하기
    for m in range(M):
        i, j = map(int, input().split())
        for k in range(1, j+1):
            left, right = i-1-k, i-1+k
            # 돌의 범위 안에 있으면
            if (0 <= left < N) and (0 <= right < N):
                # 같은지 확인하기
                if rocks[left] == rocks[right]:
                    if rocks[left] == 0:
                        # 뒤집기
                        rocks[left] = rocks[right] = 1
                    else:
                        # 뒤집기
                        rocks[left] = rocks[right] = 0
    # 출력
    print(f'#{t} {" ".join(list(map(str, rocks)))}')