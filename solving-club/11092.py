# 최대 최소의 간격
# N개의 양의 정수
# 최댓값의 위치와 최솟값의 위치의 차이 -> 절댓값 출력
# 가장 작은 수가 여러 개 : 먼저 나오는 위치, 가장 큰 수가 여러 개 : 나중에 나오는 위치

# 테스트 케이스 수
T = int(input())

# T번 반복
for t in range(1, T+1):
    # 양의 정수의 개수
    N = int(input())
    # 배열 받기
    arr = list(map(int, input().split()))
    # min, max 인덱스 가정
    min_idx = max_idx = 0

    for i in range(1, N):
        # 최댓값의 인덱스
        if arr[max_idx] <= arr[i]:
            max_idx = i
        # 최솟값의 인덱스
        if arr[min_idx] > arr[i]:
            min_idx = i

    print(f'#{t} {abs(max_idx-min_idx)}')