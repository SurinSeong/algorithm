# 배열
# 1. 입력 받은 정수를 1차원 배열에 저장하는 방법
"""
- 첫 줄에 양수의 개수 N이 주어진다. (5 <= N <= 1000)
- 다음 줄에 빈 칸으로 구분된 N개의 양수 Ai가 주어진다. (1 <= Ai <= 1000000)
6
2 7 5 3 1 4
"""

N = int(input())
arr = list(map(int, input().split()))


# 배열 연산
# 2. 배열 원소의 합 s 계산

s = 0

for i in range(N):
    s += arr[i]
    

# 3. 배열 원소 중 최댓값 max_v 찾기

max_v = arr[0]  # 첫 원소를 최대로 가정

for i in range(1, N):
    if max_v < arr[i]:
        max_v = arr[i]  # arr[i]가 더 크면 max_v 갱신
        

# 4. 배열 원소 중 최댓값의 인덱스 max_idx 찾기

max_idx = 0  # 첫 원소를 최대로 가정

for i in range(1, N):
    if arr[max_idx] < arr[i]:  # 더 큰 값을 만나면
        max_idx = i  # max_idx 갱신
        
# 위의 경우, 최댓값이 여러 개이면, 가장 왼쪽의 최댓값 인덱스의 인덱스가 max_idx가 된다.

# 5. 최댓값이 여러 개인 경우, 마지막 인덱스 max_idx 찾기

max_idx = 0  # 첫 원소를 최대로 가정

for i in range(1, N):
    if arr[max_idx] <= arr[i]:  # 더 큰 값 또는 같은 값이면
        max_idx = i  # max_idx 갱신
        

# 6. 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1을 idx에 넣기

N, V = map(int, input().split())  # N, 찾는 값 V
arr = list(map(int, input().split()))

idx = -1  # 찾는 값이 없다고 가정

for i in range(N):
    if arr[i] == V:  # arr[i]가 찾는 값이면
        idx = i  # 인덱스 저장
        break