# 최댓값이 여러 개인 경우, 마지막 인덱스 max_idx 찾기
'''
6
2 7 5 3 1 7
'''
# 원소 개수 받기
N = int(input())

# 배열 받기
arr = list(map(int, input().split()))

# max_idx 가정
max_idx = 0

# 배열 돌기
for i in range(1, N):
    # 마지막 인덱스를 찾기 위해 같다는 조건도 넣어줌.
    if arr[max_idx] <= arr[i]:
        max_idx = i
        
print(max_idx, arr[max_idx])