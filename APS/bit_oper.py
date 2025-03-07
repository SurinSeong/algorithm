"""
비트 계산 손으로 꼭 하고 넘어가기
"""

print(7 & 5)
print(7 | 5)

# 이진수 변환을 확인할 수 있음.
print(bin(7 | 5))

# 1) 이진수로 변환
# 2) 각 자리를 AND, OR 연산을 한다.

print(bin(0x4A3 | 25))


# shift 연산자
# left
print(1 << 1)
print(1 << 2)
print(1 << 3)
print(1 << 4)

# right
print(7 >> 1)

# 반복문 활용
num = 1
for _ in range(5):
    print(num)
    num = num << 1

# 비트 연산 응용
# 1. 부분집합의 수를 바로 구할 수 있음.
arr = [1, 2, 3, 4]    # 16개
# 각 집합의 해당 수를 쓰거나(1) 안쓰거나(0)로 생각하면 된다.
print(f'부분집합의 수 : {1 << len(arr)}')

for i in range(1 << len(arr)):    # 부분 집합의 수만큼 반복된다.
    for idx in range(len(arr)):    # idx : 각 자리 인덱스
        # (1 << idx) : 0b1, 0b10, 0b100, 0b1000
        if i & (1 << idx):    # i번째 부분집합에 특정 숫자가 포함되어 있는지 확인 가능 = i의 idx 번째 비트가 1인지 확인
            print(arr[idx], end=' ')
    print()

# 응용 : 합이 x인 부분집합만 출력하기 (비트 연산으로 반복문을 사용)
x = 5

for i in range(1 << len(arr)):    # 부분 집합의 수만큼 반복된다.
    subset = []    # 부분집합을 넣을 리스트
    total = 0    # 부분집합들의 합
    for idx in range(len(arr)):    # idx : 각 자리 인덱스
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]
        if total == x:    # 부분집합의 합이 x 가 되었다면
            print(f'부분집합: {subset}')    # 부분집합 출력


# 비교 : 재귀
subset = []
N = len(arr)
bit = [0] * N

def dfs(i, total, s, r):
    global x

    if total == x:    # 부분집합의 합이 x와 같다면
        print(f'부분집합: {s}')
        return

    if total > x:    # 원하는 부분집합의 합보다 크다면
        return

    # 남은 수를 더해도 부분집합의 합보다 작으면
    if x > total + r:
        return

    if i == N:    # 인덱스 범위를 넘어갔다면
        return

    s.append(arr[i])
    dfs(i+1, total+arr[i], s, r-arr[i])

    s.pop()
    dfs(i+1, total, s, r-arr[i])


print('DFS 이용')
dfs(0, 0, subset, sum(arr))