# 배열 원소의 합 s 계산하기
"""
6
2 7 5 3 1 4
"""

N = int(input())
arr = list(map(int, input().split()))

# 배열 원소의 합 s 구하기
s = 0

for i in range(N):
    s += arr[i]

print(s)