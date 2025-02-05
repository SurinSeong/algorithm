# 구간합
# N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
# M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력

# 테스트 케이스 수
T = int(input())

# 각 테스트 케이스 별 문제 풀기
for t in range(1, T+1):
    # N, M 받기
    N, M = map(int, input().split())
    # 배열 생성
    v = list(map(int, input().split()))

    # 우선 초기값 가정
    max_M, min_M = 0, 0  # 배열의 원소는 1 이상이기 때문에

    for i in range(M):
        max_M += v[i]
        min_M += v[i]

    # 배열 돌면서 합 계산
    for i in range(1, N-M+1):
        # 현재 위치에서 M개의 합 계산
        current_sum = 0
        for j in range(M):
            current_sum += v[i+j]
        # 최댓값 찾기
        if max_M < current_sum:
            max_M = current_sum
        # 최솟값 찾기
        if min_M > current_sum:
            min_M = current_sum

    print(f'#{t} {max_M - min_M}')