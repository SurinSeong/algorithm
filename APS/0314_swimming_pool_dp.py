"""
[수영장]
- 가장 적은 비용으로 수영장을 이용한다.
- 수영장에서 판매하고 있는 이용권은 4종류
- 1일 이용권
- 1달 이용권 : 매달 1일
- 3달 이용권 : 연속 3달 (11 12 1 불가능)
- 1년 이용권 : 매년 1월 1일 시작
"""
"""
DP
1. TOPDOWN
- DP (메모이제이션)
- 거듭제곱 문제

2. BOTTOMUP
- 시작점을 정해둔다.
- 앞으로 쌓아 나아가면서 진행
    - 기존값을 활용
    - 정답을 계산해서 저장하면서 진행
    => 점화식 구하는 경우가 많음.
"""


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 이용권 요금
    fare = list(map(int, input().split()))
    # 이용 계획
    planner = list(map(int, input().split()))

    answer = 0



    print(f'#{tc} {answer}')