# 화물 도크
# 24시간 운영 0~다음날0
# 최대한 많은 화물차 이용
# 앞 작업의 종료와 동시에 시작
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5202.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 신청서
    N = int(input())
    # 빈 리스트 만들기
    schedule = [0]*24
    # 신청서 리스트 만들기
    applies = [list(map(int, input().split())) for _ in range(N)]

