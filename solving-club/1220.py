import sys

sys.stdin = open('./input/input_1220.txt', 'r')

"""
[Magnetic]
- 파란색 >> N극 / 붉은색 >> S극
- 일정한 간격을 두고 강한 자기장 걸었을 때, 시간이 흐른 후 자성체들이 충돌하여 남은 교착 상태 (쌍) 확인하기
- 테이블 아래로 떨어질 수 있음.
- 반대방향으로 가는 것이 하나라도 있을 경우, 교착 상태에 빠진다.
- 빨파빨파면 2개의 교착상태
- 테이블 크기 100 x 100
- 1 : S로 간다 / 2 : N으로 간다.
- 0번 행이 N / 99행이 S
"""
# 교착상태 찾기
def find_pairs(col):
    pairs = 0    # 현재의 열에서 빨파 쌍의 개수
    magnets = []

    for row in range(N):
        if table[row][col] == 2:    # 파란색인데
            if not magnets:    # 리스트가 비어있다면
                continue    # 넣지 말기
            else:
                magnets.append(2)
        elif table[row][col] == 1:    # 빨간색이라면
            magnets.append(1)

    pre = magnets[0]
    for magnet in magnets[1:]:
        cur = magnet
        if pre != cur:    # 다른 숫자라면
            if cur == 2:
                pairs += 1
            pre = cur

    return pairs


T = 10

for tc in range(1, T+1):
    # 정사각형 테이블의 한 변의 길이
    N = int(input())
    # 테이블 초기 모습
    table = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    # 쌍을 찾기
    for col in range(N):
        answer += find_pairs(col)

    print(f'#{tc} {answer}')