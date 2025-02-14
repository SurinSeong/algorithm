# 파스칼의 삼각형
# DFS와 관련이 있음.
# DP -> 동적 계획획
# 재귀호출 -> 중복 호출(시간이 오래걸림)
"""
점화식!
이항정리와 관련이 있음.
이항정리와 이항계수
(a+b)^0 = 1
(a+b)^1 = a+b
(a+b)^2 = a^2 + 2ab + b^2
...

이항정리의 이항계수는 조합과 관련이 있다.
4C2 -> 4*3/2*1
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

4C2 = 3C1 + 3C2
"""
# nCr의 재귀적 정의 -> 점화식
# nCr = n-1Cr-1 + n-1Cr

# 조합
def combination(n, r):  # 매개변수가 중요함.
    if (r == 0) or (n == r):
        return 1
    return combination(n-1, r-1) + combination(n-1, r)

print(combination(5, 2))

# 매개변수에 대한 테이블을 만들어서 기록하는 방법도 있다.
# 1. 2차변수 만들기
memo = [[0]*101 for _ in range(101)]

def pascal(n, r):  # 매개변수가 중요함.
    if (r == 0) or (n == r):
        memo[n][r] = 1
        return 1
    
    if memo[n][r] != 0:
        return memo[n][r]
    
    memo[n][r] = combination(n-1, r-1) + combination(n-1, r)
    return memo[n][r]

print(combination(5, 3))

for i in range(6):
    print(*memo[i][:i+1])
    
# 그냥 행 순회로도 가능하다
N = 5 # => 5x5
arr = [[0]*N for _ in range(N)]

for row in arr:
    print(*arr)

for r in range(N):
    for c in range(0, r+1):
        arr[r][c] = 1
        
for row in arr:
    print(*arr)
    
for r in range(10):
    for c in range(0, r+1):
        if c == 0 or r == c:
            arr[r][c] = 1
        else:
            arr[r][c] = arr[r-1][c-1] + arr[r-1][c]
            
for i in range(N):
    print(*arr[i][:i+1])
    
    
# 재귀 호출을 할지 말지 판단은 항상 매개변수로 한다.
# 많이 그려봐야 한다.

# 인덱스 조작(반복문, 델타), 정렬 (선택, 거품), IM 보충 문제