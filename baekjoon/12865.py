"""
[평범한 배낭]
- 물건 N개
    - 무게 W, 가치 V
    - 해당 물건을 넣어서 가면 V만큼 즐긴다.

- 최대 K만큼의 무게만 넣을 수 있는 배낭
- 최대한 즐거운 여행을 할 수 있는 가져갈 물건의 개수
"""
# 최대 가치 찾기 - DFS 이용하기
def dfs(idx, remain, v):
    global max_v

    if remain == 0:
        max_v = max(max_v, v)
        return

    if idx == N:
        max_v = max(max_v, v)
        return

    if remain >= info[0][idx]:
        dfs(idx+1, remain-info[0][idx], v+info[1][idx])

    dfs(idx+1, remain, v)


# 물품의 수, 버틸 수 있는 무게
N, K = map(int, input().split())

# 물건 정보 리스트
info = [[0]*N for _ in range(2)]    # 1번행 : 무게 / 2번행 : 가치
# 물품의 수만큼 반복한다.
for i in range(N):
    # 물건의 무게, 가치
    W, V = map(int, input().split())
    info[0][i], info[1][i] = W, V

max_v = 0
dfs(0, K, 0)

print(max_v)
