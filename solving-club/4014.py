# NxN 활주로 건설
# 숫자는 지형 높이
# 가로 or 세로로 건설
# 높이(1<=<=6)가 동일한 구간에서 건설 가능
# 경사로 : 길이-2<=x<=4, 높이 1 => 경사로 높이가 극복할 수 있도록
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4014.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


# 전체 배열에서 최댓값 구하기
def find_max(arr, n):
    # 우선 가정
    max_num = max(arr[0])
    for i in range(1, n):
        max_num = max(max_num, arr[i])
    return max_num


# 경사를 넣어서 확인하기
def make_equal_height(r, x):
    """
    r : 현재의 행
    x : 경사 길이
    """
    # 첫번째 위치 부터 비교해나간다.
    previous = r[0]
    # 연속한 지형의 수
    cnt = 1
    for i in range(1, len(r)):
        # 현재 지형의 높이
        current = r[i]
        # 이전의 높이와 같으면
        if current == previous:
            # 연속 카운팅 올려주기
            cnt += 1
        # 다르면
        # 이전 높이보다 현재 높이가 높으면
        elif current > previous:
            # 카운팅 개수 확인해서 경사의 길이보다 작으면 cnt 초기화
            if cnt < x:
                cnt = 0
                # 이전의 지형 설정 변경
                previous = r[i]
            # 경사의 길이보다 크거나 같다면
            else:
                # cnt 초기화해주기
                cnt = 0
                # 경사 길이 만큼 이전 칸을 높여주자
                for k in range(1, x+1):
                    r[i-k] =


            # 이전의 것과 확인
            # 이전과 같으면
            if current == previous:
                # 카운딩
                cnt += 1
            # 다르면
            else:
                # 현재까지의 카운팅 확인
                # 경사의 길이와 같으면
                if cnt == X:
                    # 높이 올려주기
                    for k in range(X):
                        r[i-k] += 1
    if cnt == X:
        for k in range(X):
            r[i-k] += 1

    return r


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 지도의 한 변의 크기, 경사로의 길이
    N, X = input().split()
    N = int(N)
    # 지형 정보
    fields = [[int(num) for num in input().split()] for _ in range(N)]

    # 지형 변화시키기기
    for i, row in enumerate(fields):
        fields[i] = find_low_ground(row, X)
                            
    print(fields)

    print(f'#{tc}')