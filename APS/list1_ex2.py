# 배열 원소 중 최댓값 max_v 찾기
"""
6
2 7 5 3 1 4
"""

# 원소의 개수 입력 받기
N = int(input())

# 원소 입력받기
arr = list(map(int, input().split()))

# 초기 최댓값을 arr의 0번째 값으로 가정 후 찾기 시작
max_v = arr[0]

for i in range(N):
    if max_v < arr[i]:
        max_v = arr[i]

print(max_v)