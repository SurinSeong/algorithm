"""
[장훈이의 높은 선반]
- 높이 B 인 선반
- 각 점원의 키 : Hi

- 탑을 쌓아서 선반 위의 물건 사용
    - 탑 : 점원 1명 이상
    - 탑의 높이 : 점원들의 키의 합

- 높이가 B 이상인 탑 중 높이가 가장 낮은 탑
"""
def make_tower(h, start):
    global answer

    gap = h - B    # 총 높이와 선반 높이의 차이

    if gap > answer:    # 차이가 현재의 정답에 있는 차이보다 크면
        return

    if start == N:
        if gap > 0:
            answer = min(answer, gap)
        return

    if gap >= 0:
        answer = min(answer, gap)
        return

    for i in range(start, N):
        make_tower(h+H[i], i+1)



# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 점원 수, 선반의 높이
    N, B = map(int, input().split())
    # 점원들의 키
    H = list(map(int, input().split()))

    answer = B

    # 점원들의 키를 계속 합하며 진행
    make_tower(0, 0)

    print(f'#{tc} {answer}')