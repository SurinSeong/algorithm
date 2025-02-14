# N x M 배열 만들기
# 1. N, M을 입력받는다.
N, M = map(int, input().split()) # 중간 공백 넣어서 주었을 경우
# N, M = map(int, input()) # 연속으로 주었을 경우

# 2. 배열을 입력 받는다.
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)