"""
[증가하는 사탕 수열]
- 세 개의 상자
    - 첫 번째 상자 : A
    - 두 번째 상자 : B
    - 세 번째 상자 : C

[조건]
- 각 상자에 들어있는 사탕의 개수가 순증가
- 모든 상자가 비어있지 않아야 함. 1 이상

- 사탕을 먹어야 위의 두 조건을 만족할 수 있음. 그런데 안먹어도 상관없음.

[출력]
- 최소 먹어야 하는 사탕 개수는?
- 먹어치워서 조건 만족을 못하면 -1 출력
"""
def eat_candy(a, b, c):
    candies = 0

    if c <= 2:    # 조건 만족 못함.
        candies = -1
        return candies

    if c <= b:    # b가 c보다 크거나 같으면
        candies += (b - c + 1)
        b = c - 1    # c보다 하나 작게 만들어주기
        if b <= 0:    # 조건 만족 못하면
            candies = -1
            return candies

        if b <= a:    # b가 a보다 작거나 같으면
            candies += (a - b + 1)
            a = b - 1    # b보다 하나 작게 만들어주기

            if a <= 0:    # 조건 만족 못하면
                candies = -1
                return candies

            return candies

        else:    # a가 바뀐 b보다 작다면
            return candies

    if c > b:    # c가 애초에 크다면
        # a 확인
        if b > a:    # a가 b보다 작다면
            candies = 0    # 사탕 먹을 필요 없음
            return candies

        else:    # a가 b보다 크거나 같다면
            candies = a - b + 1
            a = b - 1    # 하나 줄여주고
            if a <= 0:    # 0보다 작거나 같다면
                candies = -1
                return candies

            return candies


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    answer = eat_candy(A, B, C)

    print(f'#{tc} {answer}')