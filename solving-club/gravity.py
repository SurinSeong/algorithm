# 가로 N 세로 100 크기의 방에 상자들이 쌓여있음.
# 방이 오른쪽으로 90도 회전 후 상자들이 낙하
# 가장 큰 낙차는?

# 테스트 케이스 수
T = int(input())

# 각 테스트 케이스 별 문제 풀기
for t in range(1, T+1):
    # 방의 가로 길이
    N = int(input())
    # 쌓여있는 상자의 수
    arr = list(map(int, input().split()))
    # 낙차의 최소는 0
    drop = 0

    for i in range(0, N-1):
        # i 번째 방보다 상자의 개수가 작은 방의 개수
        count = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                count += 1
        # 낙차 계산
        if drop < count:
            drop = count

    print(f'#{t} {drop}')