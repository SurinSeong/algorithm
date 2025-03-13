"""
[부분집합 합 구하기]
- 요소의 개수가 N개인 집합
- 부분 집합의 합이 S가 되는 경우의 수 구하기
"""
def get_subset(cnt, start, subset):
    global answer

    if cnt == N:
        return

    if subset > S:    # 합이 목표한 값을 넘어서면 return
        return

    if subset == S:    # 합이 목표한 값이라면
        answer += 1
        return

    for i in range(start, N+1):
        get_subset(cnt+1, i+1, subset+i)

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 요소의 개수, 합
    N, S = map(int, input().split())

    answer = 0

    get_subset(0, 1, 0)

    print(f'#{tc} {answer}')