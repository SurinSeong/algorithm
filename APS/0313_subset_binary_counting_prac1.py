"""
[도전] 친구와 카페 방문
- 민철이는 친구 {A, B, C, D, E}가 있음.
- 최소 2명 이상의 친구 선정
- 총 몇가지 경우?
"""
def get_subset(x):
    subset_list = []
    for i in range(N):
        if x & 0x1:
            subset_list.append(friends[i])
        x >>= 1

    return subset_list


friends = ['A', 'B', 'C', 'D', 'E']
N = len(friends)
cnt = 0

for target in range(1 << N):
    friend_list = get_subset(target)
    if len(friend_list) >= 2:    # 2명 이상!
        cnt += 1
        print(f'{cnt}.', end=' ')
        print(''.join(friend_list))

# ------------------------------------------------------------
## 강사님 풀이
def get_count(x):     # target 개수 반환
    cnt = 0
    for _ in range(N):
        if x & 0x1:    # if (x >> i) & 0x1:
            cnt += 1    #   cnt += 1
        x >>= 1
    return cnt


# 모든 부분집합 중 원소의 수가 2개 이상인
answer = 0

# 모든 부분 집합 확인
for target in range(1 << N):
    if get_count(target) >= 2:    # 만약 원소의 개수가 2개 이상이면
        answer += 1

print(answer)
