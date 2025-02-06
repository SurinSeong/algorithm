# 카운팅 정렬
"""
0 4 1 3 1 2 4 1 # 조건 : 0 <= DATA[i] <= 4
"""

# 배열 받기
DATA = list(map(int, input().split()))

N = len(DATA)

# 배열의 max 값 찾기
max_v = DATA[0]     # 가정
for i in range(1, N):
    if max_v < DATA[i]:
        max_v = DATA[i]

# 각 배열의 원소 개수 넣을 리스트
COUNTS = [0] * (max_v + 1)

for i in range(0, N):
    COUNTS[DATA[i]] += 1

# 누적 개수 구하기
for i in range(1, max_v+1):
    COUNTS[i] = COUNTS[i-1] + COUNTS[i]

# DATA의 뒤의 숫자에서 부터 조정
TEMP = [0] * N

for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1
    TEMP[COUNTS[DATA[i]]] = DATA[i]

    print(TEMP)