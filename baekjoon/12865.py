"""
[평범한 배낭]
- 물건 N개
    - 무게 W, 가치 V
    - 해당 물건을 넣어서 가면 V만큼 즐긴다.

- 최대 K만큼의 무게만 넣을 수 있는 배낭
- 최대한 즐거운 여행을 할 수 있는 가져갈 물건의 개수
"""
# 최대 가치 찾기 - DP 이용
# 물품의 수, 버틸 수 있는 무게
N, K = map(int, input().split())

# 물건 정보 리스트
info = [[0]*2 for _ in range(N)]    # 1번 col : 무게 / 2번 col : 가치
# 물품의 수만큼 반복한다.
for i in range(N):
    # 물건의 무게, 가치
    W, V = map(int, input().split())
    info[i][0], info[i][1] = W, V

# DP 테이블 - 열의 인덱스가 최대 무게인 곳까지 열을 추가, 행의 인덱스가 물품의 수일 때까지 행을 추가
dp = [[0] * (K+1) for _ in range(N+1)]

# DP 진행
for i in range(1, N+1):
    cw, cv = info[i-1]     # 현재 물건의 무게, 가치
    for nw in range(K+1):    # 배낭의 용량 확인하기
        if nw < cw:    # 현재 물건을 담지 못하면
            dp[i][nw] = dp[i-1][nw]    # 다음 인덱스로 현재의 무게를 옮겨준다.
        else:    # 담을 수 있을 때
            dp[i][nw] = max(dp[i-1][nw], dp[i-1][nw-cw]+cv)    # 물건을 담지 않았을 때의 가치와 담지 않았을 때의 가치 비교한다. nw-cw :

print(dp[N][K])
