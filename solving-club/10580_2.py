"""
[전봇대]
- N개의 전선으로 연결
- 일대일 대응, 교차 가능
- 세 개 이상의 전선이 하나의 점에서 만나지 않는다.
- 총 교차점의 개수는?

- 기존선과 비교하면 되겠다!
"""
# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 전선 개수
    N = int(input())
    # 두 전봇대에 있는 전선을 나타내는 배열
    cables = []
    answer = 0

    for i in range(N):    # N개의 새로운 선을 추가하면서 비교 진행
        # 전선이 걸려 있는 고도
        A, B = map(int, input().split())

        for pA, pB in cables:
            # 1. 기존의 전선보다 시작점이 높고, 도착점이 낮음
            if A > pA and B < pB:
                answer += 1
            # 2. 기존의 전선보다 시작점이 낮고, 도착점이 높음
            if A < pA and B > pB:
                answer += 1

        cables.append([A, B])

    print(f'#{tc} {answer}')