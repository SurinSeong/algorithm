# 카운팅 정렬
"""
5
3 1 5 3 2
7 4 2 9 7 6
1 5 3 4 2 1
8 6 1 7 4 6
9 2 5 1 6 8 8
"""

# 테스트 케이스 개수 받기
T = int(input())

# 테스트 케이스 돌기
for t in range(1, T+1):
    # 숫자 배열 받기
    arr = list(map(int, input().split()))
    # 숫자 배열 개수 저장
    N = len(arr)
    # 숫자 배열 중 가장 큰 값 찾기
    max_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]

    # 0부터 가장 큰 수가 마지막에 올 수 있는 count 리스트 만들기
    count = [0] * (max_v + 1)

    # 오름차순 배열된 숫자 담을 temp 리스트 생성
    temp = [0] * N

    # 1. 각 숫자의 개수를 count에 담기
    for i in range(N):
        count[arr[i]] += 1

    # 2. 누적합 구하기
    for i in range(1, max_v+1):
        count[i] += count[i-1]

    # 3. temp에 정렬시키기
    # arr의 가장 뒤의 인덱스 부터 시작하기
    for i in range(N-1, -1, -1):
        # arr의 해당 인덱스에 해당하는 원소가 count의 인덱스 인 것을 찾아 그 값을 -1 하기
        count[arr[i]] -= 1
        # count의 값이 temp의 인덱스와 같은 곳에 arr[i]를 넣기
        temp[count[arr[i]]] = arr[i]

    print(f'{t} {temp}')