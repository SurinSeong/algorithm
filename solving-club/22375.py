# 스위치 조작
# N개의 전등 1~N
# 최소 몇 개의 스위치 조작?
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_22375.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 스위치 개수
    N = int(input())
    # 조작 전
    A = list(map(int, input().split()))
    # 조작 후
    B = list(map(int, input().split()))
    # 조작 횟수 카운팅
    cnt = 0
    # 조작 전 돌면서 세어보기
    for i in range(N):
        if A[i] != B[i]:
            cnt += 1
            for k in range(i, N):
                if A[k] == 1:
                    A[k] = 0
                else:
                    A[k] = 1

    print(f'#{tc} {cnt}')
