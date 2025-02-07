# 행 우선 순회
"""
3
1 2 3
4 5 6
7 8 9
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        print(arr[i][j])