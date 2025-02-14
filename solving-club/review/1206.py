# View
# 빌딩 정보가 주어질 대, 조망권이 확보된 세대 수 반환하기
# 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보 >> 조망권 확보
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1206.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 10개
for tc in range(1, 11):
    # 건물의 개수
    N = int(input())
    # N개의 건물의 높이
    buildings = list(map(int, input().split()))
    # 조망권
    result = 0
    # 양 끝은 빼고 계산
    i = 2
    while i < N-2:
        # 현재의 건물 빼고 나머지
        sides = [i-2, i-1, i+1, i+2]

        # 양옆 두번째에서의 max 구하기
        second_max = buildings[sides[0]]
        for side in sides[1:]:
            if second_max < buildings[side]:
                second_max = buildings[side]

        # 만약 건물들 중 가장 큰 것이 현재 위치의 빌딩보다 작으면
        if second_max < buildings[i]:
            result += (buildings[i] - second_max)
            i += 3
        else:
            i += 1

    print(f'#{tc} {result}')
