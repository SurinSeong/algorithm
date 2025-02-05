# (4828)
# N개의 양의 정수에서 가장 큰 수와 작은 수의 차이를 출력

# 테스트 케이스 개수
T = int(input())
# 테스트 케이스 별로 처리
for tc in range(1, T+1):
    # 케이스 별로 입력 개수
    N = int(input())
    # 배열 입력 받기
    arr = list(map(int, input().split()))

    max_v, min_v = arr[0], arr[0] # 최대, 최솟값을 일단 배열의 0번째 원소로 가정

    for i in range(1, N):
        # 최댓값
        if max_v < arr[i]:
            max_v = arr[i]
        # 최솟값
        if min_v > arr[i]:
            min_v = arr[i]

    # 출력 방법
    print(f'#{tc} {max_v - min_v}')