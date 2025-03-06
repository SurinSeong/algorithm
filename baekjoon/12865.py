"""
[평범한 배낭]
- 물건 N개
    - 무게 W, 가치 V
    - 해당 물건을 넣어서 가면 V만큼 즐긴다.

- 최대 K만큼의 무게만 넣을 수 있는 배낭
- 최대한 즐거운 여행을 할 수 있는 가져갈 물건의 개수
"""
# 최대 가치 찾기
def find_max_value():
    global max_v

    for i in range(N):
        if K >= info[0][i]:    # 배낭에 넣을 수 있는 무게와 같거나 적으면
            remain = K - info[0][i]
            current_v = info[1][i]
            j = i+1
            while True:
                if j == N:
                    break

                remain -= info[0][j]  # 나머지 업데이트

                if remain < 0:
                    break

                current_v += info[1][j]    # 현재까지의 가치 업데이트
                j += 1  # 인덱스 업데이트

            max_v = max(max_v, current_v)


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
find_max_value()

print(max_v)
