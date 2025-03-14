"""
[수영장]
- 가장 적은 비용으로 수영장을 이용한다.
- 수영장에서 판매하고 있는 이용권은 4종류
- 1일 이용권
- 1달 이용권 : 매달 1일
- 3달 이용권 : 연속 3달 (11 12 1 불가능)
- 1년 이용권 : 매년 1월 1일 시작
"""
# 부분집합 구하는..
def select_fare():
    pass


# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # 이용권 요금
    fare = list(map(int, input().split()))
    # 이용 계획
    planner = list(map(int, input().split()))

    answer = 0

    # 이용 계획이 존재하는 달만 모아놓은 리스트
    planned_month = []

    for month in planner:
        if month > 0:
            planned_month.append(month)

    N = len(planned_month)

    dfs(0, [], 0)



    print(f'#{tc} {answer}')