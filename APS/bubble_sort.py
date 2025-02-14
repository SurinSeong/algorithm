# 버블 정렬
# 인접한 두 개의 원소를 비교하며 자리를 계속 교환
# 맨 마지막 자리에 가장 큰 수가 들어가도록 (오름차순)
'''
5
55, 7, 78, 12, 42
'''

# 원소 개수 받기
N = int(input())

# 배열 받기
arr = list(map(int, input().split()))

# 배열 돌기
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]: # 내림차순은 부등호 방향 바꾸기
            arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)
