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
    # 신청서 리스트 만들기
    applys = [list(map(int, input().split())) for _ in range(N)]
    # end로 재정렬하기
    for i in range(0, N-1):
        for j in range(i+1, N):
            if applys[i][-1] > applys[j][-1]:
                applys[i], applys[j] = applys[j], applys[i]
                
    print(applys)
        