# 배열 원소 중 최댓값의 인덱스 max_idx 찾기
"""
6
2 7 5 3 1 4
"""
# 배열의 원소의 개수 받기
N = int(input())

# 배열 받기
arr = list(map(int, input().split()))

# max_num 가정하기
max_idx = 0

# 배열 돌면서 찾기
for i in range(1, N):
    if arr[max_idx] < arr[i]:
        max_idx = i
        
print(max_idx, arr[max_idx])