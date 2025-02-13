# 쉬운 거스름돈
# s마켓에서 사용하는 돈의 종류 ~
# 거스름돈 : N
# 최소 개수는?
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1970.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')
    # 거스름돈 금액
    N = int(input())
    # 돈의 종류
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for money in moneys:
        cnt = 0
        # 가지고 있는 돈이 N보다 크다면
        if money > N:
            print(cnt, end=' ')
        # 가지고 있는 돈이 N보다 작거나 같다면
        else:
            cnt = N // money
            N %= money
            print(cnt, end=' ')
    print()

