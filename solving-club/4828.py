# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력

# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    # 양수의 개수
    N = int(input())
    # 배열 입력 받기
    arr = list(map(int, input().split()))
    # max, min 값 가정
    max_v, min_v = arr[0], arr[0]
    # for문 돌기 (index 1부터)
    for i in range(1, N):
        # 최댓값
        if max_v < arr[i]:
            max_v = arr[i]
        # 최솟값
        if min_v > arr[i]:
            min_v = arr[i]

    print(f'#{t} {max_v - min_v}')

