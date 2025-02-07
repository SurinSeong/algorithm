#  10 x 10
# 보라색 칸의 수는?

T = int(input())

for t in range(1, T+1):
    white_board = [[0] * 10 for _ in range(10)]
    # 색칠 횟수
    N = int(input())
    purple = 0
    for _ in range(N):
        # 어디 색칠할까?
        x1, y1, x2, y2, color = map(int, input().split())
        purple += color