# 백만장자 프로젝트
# 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있음.
# 하루에 최대 1만큼 구입 가능
# 판매는 얼마든지 가능
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1859.txt'
sys.stdin = open(filename, 'r')


# 함수
# 맨 앞에서부터 빼가면서 수가 0 이상이면 계속 가기
def find_max_profit(days):
    """
    애초에 날짜를 받을 때 제일 최근 날짜로 받는다.
    """
    max_day = days[0]
    profits = 0
    for day in days[1:]:
        # 양수면 유지
        if max_day - day > 0:
            profits += (max_day - day)
        else:
            max_day = day

    return profits


# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # 연속된 N일
    N = int(input())
    # 매매가
    trade = list(map(int, input().split()))
    result = find_max_profit(trade[::-1])

    print(f'#{t} {result}')
