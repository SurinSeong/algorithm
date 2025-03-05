"""
[깃발 게임 결승전]
- 팀 개수 : T
- 난이도 2의 명령만 수행함.
- 팀원 : N명 1~N
- M번의 명령 => 양의 정수 a(난이도) b(기준 번호) c(비교 범위)
- a == 2이면,
    - b자리에서 양 옆의 칸의 깃발 상태가 다르면 상태유지하고
    - 같으면 둘다 상태 바꾼다.
    - c 만큼 반복한다.
"""
# 깃발 변경 함수
def change_position(l, r):
    if first_position[l] == first_position[r]:
        first_position[l] = 1 - first_position[l]
        first_position[r] = 1 - first_position[r]


# 팀 개수
T = int(input())

for team in range(1, T+1):
    # 팀원 수, 명령 수
    N, M = map(int, input().split())
    # 초기 상태
    first_position = list(map(int, input().split()))
    # 명령 개수 만큼 명령이 나온다.
    for _ in range(M):
        a, b, c = map(int, input().split())

        for k in range(1, c+1):
            left, right = (b-1)-k, (b-1)+k
            if (0 <= left < N) and (0 <= right < N):    # 범위 안에 있다면 명령 수행한다.
                change_position(left, right)

    result = list(map(str, first_position))

    print(f'#{team} {" ".join(result)}')