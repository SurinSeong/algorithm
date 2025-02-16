# 농작물 수확하기
# NxN 농장
# 마름모 ==> 중간을 0,0로 생각해서 공식 구해보기
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_2805.txt'
sys.stdin = open(filename, 'r')


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 농장의 크기
    N = int(input())
    # 농작물의 가치
    fields = [list(map(int, input())) for _ in range(N)]
    # 총 수확량
    total = 0
    

    print(f'#{tc} {total}')
