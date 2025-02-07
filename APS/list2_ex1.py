# 2차원 배열

"""
3
1 2 3
4 5 6
7 8 9
"""

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

print(matrix)

"""
3
123
456
789
"""

N = int(input())

matrix = [list(map(int, input())) for _ in range(N)]
print(matrix)